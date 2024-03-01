import logging
import os

from app.core.models.ollama import OllamaWrapper
from app.core.models.openai import OpenAIWrapper
from app.helpers.constants import Models
from app.helpers.logging import setup_logger

logger = setup_logger('ModelSelector')


class ModelSelector:
    @staticmethod
    def select_default():
        selected_model = os.getenv('MODEL')
        if not selected_model:
            selected_model = 'MISTRAL'

        if selected_model == 'GPT3_5':
            model = OpenAIWrapper(Models.GPT3_5)
        elif selected_model == 'MISTRAL':
            model = OllamaWrapper(Models.MISTRAL)
        elif selected_model == 'QWEN7B':
            model = OllamaWrapper(Models.QWEN7B)
        elif selected_model == 'PHI':
            model = OllamaWrapper(Models.PHI)
        elif selected_model == 'GEMMA':
            model = OllamaWrapper(Models.GEMMA)
        else:
            raise ValueError(f"Invalid model selection {selected_model}, available types: GPT3_5, MISTRAL")

        logger.info(f"Using {selected_model} Model")
        return model
