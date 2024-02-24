from app.core.models.base import BaseModel
from app.helpers.constants import ModelDetails as M

import os

from langchain_openai import ChatOpenAI


class OpenAIModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.llm = None
        self.load()

    def load(self, model_type=M.GPT3_5):
        openai_api_key = os.getenv("OPEN_AI_API_KEY")
        if not openai_api_key:
            raise ValueError("No API key set. Please set the OPEN_AI_API_KEY env var")

        if model_type == M.GPT3_5:
            self.llm = ChatOpenAI(model_name=M.GPT3_5['name'], openai_api_key=openai_api_key)



