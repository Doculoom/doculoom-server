import json
import os

from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import OpenAIEmbeddings

from app.helpers.constants import Prompts


class Agent:
    def __init__(self, llm, base_dir='data'):
        self.chat_history = None
        self.llm = llm
        self.base_dir = base_dir
        self.conv_dir = base_dir + '/conversations'
        self.doc_dir = base_dir + '/docs'
        self.index_dir = base_dir + '/index'
        self.text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
        self.embeddings = OpenAIEmbeddings()
        self.chain = None
        self.db = None
        self.loaded_doc = None
        self.loaded_chat_history = None

        if not os.path.exists(self.conv_dir):
            os.makedirs(self.conv_dir)

        if not os.path.exists(self.doc_dir):
            os.makedirs(self.doc_dir)

        if not os.path.exists(self.index_dir):
            os.makedirs(self.index_dir)

    def create_chain(self, db):
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Answer the user's questions based on the context: {context}"),
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}")
        ])

        chain = create_stuff_documents_chain(
            llm=self.llm,
            prompt=prompt
        )

        retriever = db.as_retriever(search_kwargs={"k": 3})

        retriever_prompt = ChatPromptTemplate.from_messages([
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
            ("user", Prompts.USE_CONTEXT_AND_ANSWER)
        ])
        history_aware_retriever = create_history_aware_retriever(
            llm=self.llm,
            retriever=retriever,
            prompt=retriever_prompt
        )

        retrieval_chain = create_retrieval_chain(
            history_aware_retriever,
            chain
        )

        return retrieval_chain

    def chat(self, doc_name, message):
        self.load_doc(doc_name)
        self.load_chat_history(doc_name)

        response = self.chain.invoke({
            "chat_history": self.chat_history.messages,
            "input": message,
        })

        self.chat_history.add_user_message(message)
        self.chat_history.add_ai_message(response["answer"])
        return response["answer"]

    def clear_chat_history(self, doc_name):
        if not self.chat_history:
            self.load_chat_history(doc_name)
        self.chat_history.clear()

    def index_and_save(self, name, content):
        doc_path = self.save_document(name, content)
        index_path = f"{self.index_dir}/{name}"

        loader = TextLoader(doc_path)
        documents = loader.load()

        docs = self.text_splitter.split_documents(documents)
        FAISS.from_documents(docs, self.embeddings).save_local(index_path)

    def check_index(self, name):
        index_path = f"{self.index_dir}/{name}"
        exists = os.path.exists(index_path)
        return exists

    def load_doc(self, name):
        if self.loaded_doc != name:
            index_path = f"{self.index_dir}/{name}"
            self.loaded_doc = name
            self.db = FAISS.load_local(index_path, embeddings=self.embeddings)
            self.chain = self.create_chain(self.db)

    def save_document(self, name, content):
        doc_path = f"{self.doc_dir}/{name}.txt"
        with open(doc_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return doc_path

    def load_chat_history(self, doc_name):
        if self.loaded_chat_history != doc_name:
            filepath = os.path.join(self.conv_dir, f"{doc_name}.json")
            self.chat_history = FileChatMessageHistory(filepath)
            self.loaded_chat_history = doc_name

    def get_chat_messages(self, doc_name):
        filepath = os.path.join(self.conv_dir, f"{doc_name}.json")
        with open(filepath, 'r', encoding='utf-8') as file:
            message_history = json.load(file)

        messages = []
        for message in message_history:
            messages.append({
                'entity': message['type'],
                'message': message['data']['content']
            })

        return messages
