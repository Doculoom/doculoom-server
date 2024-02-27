import os

from app.core.models.ollama import OllamaWrapper
from app.core.models.openai import OpenAIWrapper
from app.helpers.constants import Models


class ModelSelector:
    @staticmethod
    def select_default():
        selected_model = os.getenv('MODEL', 'MISTRAL')

        if selected_model == 'GPT3_5':
            return OpenAIWrapper(Models.GPT3_5)
        elif selected_model == 'MISTRAL':
            return OllamaWrapper(Models.MISTRAL)
        else:
            raise ValueError(f"Invalid model selection, available types: {['GPT3_5', 'MISTRAL']}")
