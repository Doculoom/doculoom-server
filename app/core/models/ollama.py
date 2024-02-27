from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms.ollama import Ollama

from app.core.models.base import BaseModel


class OllamaWrapper(BaseModel):
    def __init__(self, model_type):
        super().__init__()
        self.model_type = model_type
        self.model_name = model_type["name"]
        self.set_llm()
        self.set_embeddings()

    def set_llm(self):
        self.llm = Ollama(model=self.model_name)
        self.embeddings = OllamaEmbeddings(model=self.model_name)

    def set_embeddings(self):
        self.embeddings = OllamaEmbeddings(model=self.model_name)
