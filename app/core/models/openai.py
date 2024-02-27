from app.core.models.base import BaseModel

import os

from langchain_openai import ChatOpenAI, OpenAIEmbeddings


class OpenAIWrapper(BaseModel):
    def __init__(self, model_type):
        super().__init__()
        self.model_type = model_type
        self.model_name = model_type['name']
        self.set_llm()
        self.set_embeddings()

    def set_llm(self):
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("No API key set. Please set the OPENAI_API_KEY env var")

        self.llm = ChatOpenAI(model_name=self.model_name, openai_api_key=openai_api_key)

    def set_embeddings(self):
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("No API key set. Please set the OPENAI_API_KEY env var")

        self.embeddings = OpenAIEmbeddings()



