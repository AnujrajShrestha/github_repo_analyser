import streamlit as st
from langchain_core.messages import HumanMessage

from git_clone import clone_repo
from db import run_db
from agentic import app
from report_maker import create_report

st.set_page_config(
    page_title="GitHub Repository Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI GitHub Repository Analyzer")

st.write(
    """
Analyze any public GitHub repository using **LangGraph + RAG + Mistral AI**.

The AI will generate:

- 📄 Project Summary
- 🏗 Architecture Analysis
- 🔍 Code Review
"""
)

repo_url = st.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/username/repository"
)

if st.button("Analyze Repository", use_container_width=True):

    if repo_url == "":
        st.warning("Please enter a GitHub repository URL.")
        st.stop()

    with st.spinner("Cloning repository..."):
        clone_repo(repo_url)

    with st.spinner("Creating vector database..."):
        retriever = run_db(repo_url)

    with st.spinner("Analyzing repository..."):

        result = app.invoke(
            {
                "repo_url": repo_url,
                "retriever": retriever,
                "messages": [
                    HumanMessage(
                        content="Summarize, analyze and review this repository."
                    )
                ],
            }
        )

    report_path = create_report(result)

    st.success("Analysis Completed!")

    tab1, tab2, tab3 = st.tabs(
        [
            "📄 Summary",
            "🏗 Architecture",
            "🔍 Code Review"
        ]
    )

    with tab1:
        st.markdown(result["summary"])

    with tab2:
        st.markdown(result["architecture"])

    with tab3:
        st.markdown(result["review"])

    with open(report_path, "rb") as file:
        st.download_button(
            "📥 Download Report",
            file,
            file_name="github_report.txt",
            mime="text/plain",
            use_container_width=True,
        )