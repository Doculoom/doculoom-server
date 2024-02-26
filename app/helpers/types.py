from typing import Optional

from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str


class DocRequest(BaseModel):
    doc_url: Optional[str] = None
    doc_hash: str
    content: str
