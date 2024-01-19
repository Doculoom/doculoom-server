import os
import asyncio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

load_dotenv()  # Load environment variables from .env file
LLM_API_KEY = os.getenv('LLM_API_KEY')

app = FastAPI()

# Set up LangChain with OpenAI
llm = OpenAI(openai_api_key=LLM_API_KEY)

class LlmAgent():
    def __init__(self):
        template = """Question: {question}\n\nAnswer: Let's think step by step."""
        self.prompt = PromptTemplate(template=template, input_variables=["question"])
        self.llm_chain = LLMChain(prompt=self.prompt, llm=llm)

    def run(self, input_text):
        return self.llm_chain.run(input_text)

llm_agent = LlmAgent()  # Create an instance of LlmAgent

class ChatInput(BaseModel):
    input: str

async def query_llm(input_text: str) -> str:
    response = await asyncio.to_thread(llm_agent.run, input_text)
    return response

@app.post("/chat")
async def chat(request_body: ChatInput):
    try:
        llm_response = await query_llm(request_body.input)
        return {"message": llm_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
