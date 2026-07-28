from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from typing import TypedDict,Annotated
from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages
from db import load_context

load_dotenv()

llm= ChatMistralAI(model="mistral-large-latest",temperature=0.5)

class State(TypedDict):
    repo_url: str
    retriever: object
    messages: Annotated[list, add_messages]
    summary: dict
    architecture: dict
    review: dict
    

def summary_node(state: State) -> dict:
    print("Summary agent is working...\n")
    query= state['messages'][-1].content
    context= load_context(state['retriever'],query)
    SUMMARY_PROMPT = ("""
You are a senior software engineer.

Analyze the provided GitHub repository.

Generate a concise project summary.

Include:

1. Project Name
2. Purpose
3. Main Features
4. Primary Programming Language
5. Frameworks Used
6. Folder Structure Overview
7. Who would use this project?
"""
f"context: {context}")

    response= llm.invoke(SUMMARY_PROMPT)
    return {"summary": response.content}


def architecture_node(state: State) -> dict:
    print("Architecture agent is working...\n")
    query= state['messages'][-1].content
    context= load_context(state['retriever'],query)
    ARCHITECTURE_PROMPT = ("""
    You are a software architect.
    
    Analyze the repository architecture.
    
    Explain:
    
    1. Overall architecture
    2. Major modules
    3. Responsibilities of each module
    4. Data flow
    5. Dependency relationships
    6. Entry point
    7. Database usage
    8. AI components
    9. APIs
    10. Suggestions to improve architecture
    """ 
    f"Repository:{context}")
    response= llm.invoke(ARCHITECTURE_PROMPT)
    return {"architecture": response.content}

def review_node(state: State) -> dict:
    print("Review agent is working...\n")
    query=state["messages"][-1].content
    context= load_context(state['retriever'],query)
    REVIEW_PROMPT = ("""
You are an experienced code reviewer.

Review the repository.

Analyze:

1. Code Quality
2. Readability
3. Naming conventions
4. Project Structure
5. Error Handling
6. Security Issues
7. Performance Issues
8. Code Duplication
9. Missing Documentation
10. Best Practice Violations

Provide actionable suggestions.
"""
f"Repository: {context}")
    
    response= llm.invoke(REVIEW_PROMPT)

    return {"review": response.content}

graph= StateGraph(State)
graph.add_node("summary",summary_node)
graph.add_node("architecture",architecture_node)
graph.add_node("review",review_node)

graph.add_edge(START,"summary")
graph.add_edge(START,"architecture")
graph.add_edge(START,"review")

graph.add_edge("summary",END)
graph.add_edge("architecture",END)
graph.add_edge("review",END)


app= graph.compile()