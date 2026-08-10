from agentic import app
from langchain_core.messages import HumanMessage
from report_maker import create_report

from url import run_url

def run_pipeline():
    repo= run_url()
    result = app.invoke(
    {
        "repo_url": repo["url"],
        "retriever": repo["retriever"],
        "messages": [
            HumanMessage(
                content="Summarize, analyze and review this repository."
            )
        ],
    }
)
    
    
    print("Github public repositority analyser")
    print("-"*50)
    print("Summary:\n")
    print(result['summary'])
    print("-"*50)
    print("Architecture:\n")
    print(result['architecture'])
    print("-"*50)
    print("Review:\n")
    print(result['review'])
    print("-"*50)
    
    create_report(result)

if __name__== "__main__":
    run_pipeline()