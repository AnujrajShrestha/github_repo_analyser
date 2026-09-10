from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl

from rag_engine import run_pipeline, load_context
from llms import chat_chain

from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage
)


app = FastAPI(
    title="GitHub Repository Analyzer API"
)


# =========================================================
# CORS
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# Request Models
# =========================================================

class RepositoryRequest(BaseModel):
    url: HttpUrl


class ChatRequest(BaseModel):
    query: str


# =========================================================
# Chat History
# =========================================================

message_history = [
    SystemMessage(
        content="You are a helpful AI GitHub repository assistant."
    )
]


# =========================================================
# Home
# =========================================================

@app.get("/")
def home():
    return {
        "message": "GitHub Repository Analyzer API is running"
    }


# =========================================================
# Analyze
# =========================================================

@app.post("/analyze")
def analyze_repository(request: RepositoryRequest):

    try:

        result = run_pipeline(str(request.url))

        return {
            "status": "success",
            "repository": str(request.url),
            "analysis": result["analysis_result"],
            "summary": result["summarize_result"],
            "review": result["review_result"]
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =========================================================
# Chat
# =========================================================

@app.post("/chat")
def chat_repository(request: ChatRequest):

    try:

        context = load_context(request.query)

        result = chat_chain.invoke(
            {
                "history": message_history,
                "context": context,
                "query": request.query
            }
        )

        answer = result.response

        message_history.append(
            HumanMessage(content=request.query)
        )

        message_history.append(
            AIMessage(content=answer)
        )

        return {
            "status": "success",
            "question": request.query,
            "response": answer
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )