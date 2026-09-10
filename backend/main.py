import sys
from pathlib import Path

# Add project root to Python path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl

from RAG_engine.rag_engine import run_pipeline, load_context
from RAG_engine.llms import chat_chain

from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage
)


app = FastAPI(
    title="GitHub Repository Analyzer API"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RepositoryRequest(BaseModel):
    url: HttpUrl


class ChatRequest(BaseModel):
    query: str


message_history = [
    SystemMessage(
        content="You are a helpful AI GitHub repository assistant."
    )
]


@app.get("/")
def home():
    return {
        "message": "GitHub Repository Analyzer API is running"
    }


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