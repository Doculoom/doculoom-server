class BaseModel:
    def __init__(self):
        self.llm = None
        self.embeddings = None
        self.model_name = None

    def set_llm(self):
        raise NotImplementedError

    def set_embeddings(self):
        raise NotImplementedError


