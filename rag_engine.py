from git_clone import clone_repo
from db import run_db
from llms import analysis_chain,summary_chain,chat_chain,review_chain
from report_maker import create_report

from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()
embedding_model= MistralAIEmbeddings(model='mistral-embed')
message=[
    SystemMessage(content="You are a helpful AI assistant, your task is to analyis the files")
]

def load_context(query):
    vectorStore= Chroma(
        persist_directory='repo_db',
        embedding_function= embedding_model
    )

    retriever= vectorStore.as_retriever(
        search_type='mmr',
        search_kwargs={
            "k":8,
            "fetch_k":12,
            "lambda_mult":0.5
        }
    )

    docs= retriever.invoke(query)
    context= "\n\n".join(doc.page_content for doc in docs)
    return context

def run_pipeline(user_input):
    state={}
    clone_repo(user_input)
    run_db(user_input)
    
    context= load_context("provide the information,summary and suggestion of this project.")

    print("\n"+" -"*50)
    print("Step 1 - Analysis agent is working ...")
    print("\n"+" -"*50)
    
    analysis = analysis_chain.invoke({
        "query": "Analyze the repository.",
        "context": context
    })
    state['analysis_result']= analysis.model_dump()
    print("\nAnalysis results: \n")
    for name, value in state["analysis_result"].items():
       print(f"\n{name}: {value}\n")
       
    print("\n"+" -"*50)
    print("Step 2 - Summarize agent is working ...")
    print("\n"+" -"*50)

    summary = summary_chain.invoke({
        "query": "Summarize the repository.",
        "context": context
    })
    state['summarize_result']= summary.model_dump()
    print("\nSummarize results: \n")
    for name, value in state["summarize_result"].items():
       print(f"\n{name}: {value}\n")

    print("\n"+" -"*50)
    print("Step 3 - Review agent is working ...")
    print("\n"+" -"*50)
    review = review_chain.invoke({
        "query": "Review the repository.",
        "context": context
    })
    state['review_result']= review.model_dump()
    print("\nReview results: \n")
    for name, value in state["review_result"].items():
       print(f"\n{name}: {value}\n")
    
    create_report(state)
    return state

def chat_wela_llm():
    print("Chat with repository")
    print("\n----------How can I help you today ?-------------\n")
    print("Type 0 to exit the application")

    while True:
        query = input("You: ")

        if query == "0":
            break

        context = load_context(query)

        res_object = chat_chain.invoke({
            "history": message,
            "context": context,
            "query": query
        })

        bot_reply = res_object.response

        message.append(HumanMessage(content=query))
        message.append(AIMessage(content=bot_reply))

        print("\nBot:", bot_reply)

if __name__=="__main__":
    user_input= input("Enter repository url: ")
    run_pipeline(user_input)
    print("\n"+" -"*50)
    print("Step 4 - Chat agent is Loaded ...")
    print("\n"+" -"*50)
    chat_wela_llm()