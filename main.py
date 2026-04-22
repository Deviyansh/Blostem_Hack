from fastapi import FastAPI
from pydantic import BaseModel
from processor import FinancialAdvisor

app = FastAPI()
advisor = FinancialAdvisor()

class ChatRequest(BaseModel):
    message: str
    language: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    response = advisor.get_simplified_explanation(request.message, request.language)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)