import streamlit as st
from rag_engine import run_pipeline, load_context
from llms import chat_chain
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

st.set_page_config(
    page_title="GitHub Repository Analyzer",
    page_icon="📂",
    layout="wide"
)

# ---------------- Session State ---------------- #

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "summary" not in st.session_state:
    st.session_state.summary = None

if "review" not in st.session_state:
    st.session_state.review = None

if "history" not in st.session_state:
    st.session_state.history = [
        SystemMessage(content="You are a GitHub Repository Assistant.")
    ]


# ---------------- Header ---------------- #

st.title("📂 GitHub Repository Analyzer")
st.caption("Analyze any public GitHub repository using RAG + LangChain + Mistral + Groq")


repo_url = st.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/user/project"
)

analyze = st.button("Analyze Repository", type="primary")


# ---------------- Analyze ---------------- #

if analyze:

    if repo_url == "":
        st.warning("Please enter repository URL.")
        st.stop()

    progress = st.progress(0)

    status = st.empty()

    status.info("Cloning Repository...")
    progress.progress(10)

    with st.spinner("Analyzing repository..."):
        result = run_pipeline(repo_url)

    progress.progress(100)
    status.success("Repository analyzed successfully!")

    st.session_state.analysis = result["analysis_result"]
    st.session_state.summary = result["summarize_result"]
    st.session_state.review = result["review_result"]


# ---------------- Tabs ---------------- #

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📊 Analysis",
        "📝 Summary",
        "⭐ Review",
        "💬 Chat"
    ]
)

# ===================================================
# Analysis
# ===================================================

with tab1:

    if st.session_state.analysis:

        data = st.session_state.analysis

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Files", data["total_files"])
            st.metric("Folders", data["total_folders"])

        with col2:
            st.metric("Project", data["project_name"])
            st.metric("Type", data["project_type"])

        st.divider()

        st.subheader("Languages")

        st.write(data["programming_languages"])

        st.subheader("Frameworks")

        st.write(data["frameworks"])

        st.subheader("Dependencies")

        st.write(data["dependencies"])

        st.subheader("Entry Points")

        st.write(data["entry_points"])

        st.subheader("Important Files")

        st.write(data["important_files"])

        st.subheader("Folder Structure")

        for folder in data["folder_structure"]:
            st.code(folder)

    else:
        st.info("Analyze a repository first.")


# ===================================================
# Summary
# ===================================================

with tab2:

    if st.session_state.summary:

        data = st.session_state.summary

        st.header(data["project_name"])

        st.write(data["summary"])

        st.divider()

        st.subheader("Purpose")

        st.write(data["purpose"])

        st.subheader("Category")

        st.write(data["project_category"])

        st.subheader("Tech Stack")

        st.write(data["tech_stack"])

        st.subheader("Key Features")

        for feature in data["key_features"]:
            st.success(feature)

    else:
        st.info("Analyze repository first.")


# ===================================================
# Review
# ===================================================

with tab3:

    if st.session_state.review:

        data = st.session_state.review

        st.metric(
            "Overall Score",
            f'{data["overall_score"]}/10'
        )

        st.divider()

        c1, c2 = st.columns(2)

        with c1:

            st.subheader("Strengths")

            for s in data["strengths"]:
                st.success(s)

        with c2:

            st.subheader("Weaknesses")

            for w in data["weaknesses"]:
                st.error(w)

        st.divider()

        st.subheader("Code Quality")

        st.write(data["code_quality"])

        st.subheader("Documentation")

        st.write(data["documentation_quality"])

        st.subheader("Project Structure")

        st.write(data["project_structure"])

        st.subheader("Maintainability")

        st.write(data["maintainability"])

        st.subheader("Scalability")

        st.write(data["scalability"])

        st.subheader("Security Issues")

        for item in data["security_issues"]:
            st.warning(item)

        st.subheader("Performance Issues")

        for item in data["performance_issues"]:
            st.warning(item)

        st.subheader("Suggestions")

        for item in data["suggestions"]:
            st.info(item)

        st.subheader("Final Review")

        st.write(data["final_review"])

    else:
        st.info("Analyze repository first.")


# ===================================================
# Chat
# ===================================================

with tab4:

    st.subheader("Chat with Repository")

    question = st.chat_input("Ask anything about the repository")

    if question:

        context = load_context(question)

        response = chat_chain.invoke(
            {
                "history": st.session_state.history,
                "context": context,
                "query": question
            }
        )

        answer = response.response

        st.session_state.history.append(
            HumanMessage(content=question)
        )

        st.session_state.history.append(
            AIMessage(content=answer)
        )

    for msg in st.session_state.history[1:]:

        if isinstance(msg, HumanMessage):

            with st.chat_message("user"):
                st.write(msg.content)

        else:

            with st.chat_message("assistant"):
                st.write(msg.content)