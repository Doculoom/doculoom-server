from fastapi import APIRouter, HTTPException

from app.core.agent import Agent
from app.helpers.model_selector import ModelSelector
from app.helpers.types import ChatRequest, DocRequest

router = APIRouter()

model = ModelSelector.select_default()
agent = Agent(model)


@router.post('/')
async def process_doc(request: DocRequest):
    try:
        agent.index_and_save(name=request.doc_hash, content=request.content)
        return {"status": "OK", "message": f"Document content has been processed."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/{doc_hash}')
async def check_index(doc_hash: str):
    response = agent.check_index(doc_hash)
    if response:
        return {"status": "OK", "message": f"Document with hash {doc_hash} found."}
    else:
        raise HTTPException(status_code=400, detail=f"Document with hash {doc_hash} not found.")


@router.get('/{doc_hash}/history/')
async def get_chat_history(doc_hash: str):
    messages = agent.get_chat_messages(doc_name=doc_hash)
    return {"status": "OK", "message": messages}


@router.delete('/{doc_hash}/history/')
async def clear_history(doc_hash: str):
    agent.clear_chat_history(doc_hash)
    return {"status": "OK", "message": f"Chat history has been deleted."}


@router.post('/{doc_hash}/chat')
async def chat(doc_hash: str, request: ChatRequest):
    response = agent.chat(doc_hash, request.question)
    return {"response": response}

