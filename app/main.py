from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.post("/chat")
async def chat(request_body: dict):
    try:
        response = {'message': f"Echo: {request_body.get('input', '')}"}
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
