import streamlit as st
import requests


# =========================================================
# CONFIGURATION
# =========================================================

API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="GitHub Repository Analyzer",
    page_icon="🤖",
    layout="wide"
)


# =========================================================
# SESSION STATE
# =========================================================

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "summary" not in st.session_state:
    st.session_state.summary = None

if "review" not in st.session_state:
    st.session_state.review = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# =========================================================
# HEADER
# =========================================================

st.title("🤖 GitHub Repository Analyzer")

st.markdown(
    """
    Analyze any public GitHub repository using:

    **FastAPI + LangChain + RAG + ChromaDB + Groq + Mistral**
    """
)

st.divider()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("⚙️ Settings")

    st.write("Backend API")

    st.code(API_URL)

    st.divider()

    if st.button("🗑️ Clear Results"):

        st.session_state.analysis = None
        st.session_state.summary = None
        st.session_state.review = None
        st.session_state.chat_history = []

        st.rerun()


# =========================================================
# REPOSITORY INPUT
# =========================================================

st.subheader("🔗 Repository")

repo_url = st.text_input(
    "Enter GitHub repository URL",
    placeholder="https://github.com/username/repository"
)


# =========================================================
# ANALYZE BUTTON
# =========================================================

if st.button(
    "🚀 Analyze Repository",
    type="primary",
    use_container_width=True
):

    if not repo_url.strip():

        st.warning("Please enter a GitHub repository URL.")

    else:

        try:

            with st.spinner(
                "Cloning, indexing and analyzing repository..."
            ):

                response = requests.post(
                    f"{API_URL}/analyze",
                    json={
                        "url": repo_url
                    },
                    timeout=600
                )


            # ---------------------------------------------
            # SUCCESS
            # ---------------------------------------------

            if response.status_code == 200:

                result = response.json()

                st.session_state.analysis = result.get(
                    "analysis"
                )

                st.session_state.summary = result.get(
                    "summary"
                )

                st.session_state.review = result.get(
                    "review"
                )

                st.session_state.chat_history = []

                st.success(
                    "✅ Repository analyzed successfully!"
                )

            # ---------------------------------------------
            # API ERROR
            # ---------------------------------------------

            else:

                try:
                    error = response.json()

                    st.error(
                        f"API Error: {error.get('detail', error)}"
                    )

                except Exception:

                    st.error(
                        f"API Error: {response.text}"
                    )


        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Could not connect to FastAPI backend."
            )

            st.info(
                "Make sure FastAPI is running with:\n\n"
                "`uvicorn main:app --reload`"
            )


        except requests.exceptions.Timeout:

            st.error(
                "⏱️ Request timed out. "
                "Repository analysis is taking too long."
            )


        except Exception as e:

            st.error(
                f"Unexpected error: {str(e)}"
            )


# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📊 Analysis",
        "📝 Summary",
        "⭐ Review",
        "💬 Chat"
    ]
)


# =========================================================
# TAB 1 — ANALYSIS
# =========================================================

with tab1:

    if st.session_state.analysis:

        data = st.session_state.analysis

        st.header("📊 Repository Analysis")

        # ---------------------------------------------
        # Metrics
        # ---------------------------------------------

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Project",
                data.get("project_name", "N/A")
            )

        with col2:

            st.metric(
                "Files",
                data.get("total_files", 0)
            )

        with col3:

            st.metric(
                "Folders",
                data.get("total_folders", 0)
            )

        with col4:

            st.metric(
                "Project Type",
                data.get("project_type", "N/A")
            )

        st.divider()

        # ---------------------------------------------
        # Root Directory
        # ---------------------------------------------

        st.subheader("📁 Root Directory")

        st.code(
            data.get("root_directory", "N/A")
        )

        # ---------------------------------------------
        # Languages
        # ---------------------------------------------

        st.subheader("💻 Programming Languages")

        languages = data.get(
            "programming_languages",
            []
        )

        if languages:

            cols = st.columns(
                min(len(languages), 4)
            )

            for i, language in enumerate(languages):

                cols[i % len(cols)].success(
                    language
                )

        else:

            st.info("No languages detected.")

        # ---------------------------------------------
        # Frameworks
        # ---------------------------------------------

        st.subheader("🧩 Frameworks")

        frameworks = data.get(
            "frameworks",
            []
        )

        if frameworks:

            st.write(
                ", ".join(frameworks)
            )

        else:

            st.info("No frameworks detected.")

        # ---------------------------------------------
        # Dependencies
        # ---------------------------------------------

        st.subheader("📦 Dependencies")

        dependencies = data.get(
            "dependencies",
            []
        )

        if dependencies:

            for dependency in dependencies:

                st.write(
                    f"• {dependency}"
                )

        else:

            st.info("No dependencies detected.")

        # ---------------------------------------------
        # Entry Points
        # ---------------------------------------------

        st.subheader("🚪 Entry Points")

        entry_points = data.get(
            "entry_points",
            []
        )

        for entry in entry_points:

            st.code(entry)

        # ---------------------------------------------
        # Important Files
        # ---------------------------------------------

        st.subheader("⭐ Important Files")

        important_files = data.get(
            "important_files",
            []
        )

        for file in important_files:

            st.write(
                f"📄 {file}"
            )

        # ---------------------------------------------
        # Folder Structure
        # ---------------------------------------------

        st.subheader("🌳 Folder Structure")

        structure = data.get(
            "folder_structure",
            []
        )

        if structure:

            st.code(
                "\n".join(structure),
                language="text"
            )

    else:

        st.info(
            "👆 Enter a GitHub repository URL "
            "and click **Analyze Repository**."
        )


# =========================================================
# TAB 2 — SUMMARY
# =========================================================

with tab2:

    if st.session_state.summary:

        data = st.session_state.summary

        st.header(
            f"📝 {data.get('project_name', 'Project Summary')}"
        )

        st.subheader("🎯 Purpose")

        st.write(
            data.get(
                "purpose",
                "Not available"
            )
        )

        st.subheader("🏷️ Project Category")

        st.info(
            data.get(
                "project_category",
                "Not available"
            )
        )

        st.subheader("🚀 Key Features")

        features = data.get(
            "key_features",
            []
        )

        for feature in features:

            st.success(
                f"✓ {feature}"
            )

        st.subheader("🛠️ Technology Stack")

        tech_stack = data.get(
            "tech_stack",
            []
        )

        if tech_stack:

            st.write(
                " • ".join(tech_stack)
            )

        st.subheader("📖 Project Overview")

        st.write(
            data.get(
                "summary",
                "No summary available."
            )
        )

    else:

        st.info(
            "Analyze a repository to generate its summary."
        )


# =========================================================
# TAB 3 — REVIEW
# =========================================================

with tab3:

    if st.session_state.review:

        data = st.session_state.review

        st.header("⭐ Repository Review")

        # ---------------------------------------------
        # Score
        # ---------------------------------------------

        score = data.get(
            "overall_score",
            0
        )

        st.metric(
            "Overall Score",
            f"{score}/10"
        )

        st.divider()

        # ---------------------------------------------
        # Strengths / Weaknesses
        # ---------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("✅ Strengths")

            strengths = data.get(
                "strengths",
                []
            )

            for strength in strengths:

                st.success(
                    strength
                )

        with col2:

            st.subheader("⚠️ Weaknesses")

            weaknesses = data.get(
                "weaknesses",
                []
            )

            for weakness in weaknesses:

                st.warning(
                    weakness
                )

        st.divider()

        # ---------------------------------------------
        # Code Quality
        # ---------------------------------------------

        st.subheader("💻 Code Quality")

        st.write(
            data.get(
                "code_quality",
                "Not available"
            )
        )

        # ---------------------------------------------
        # Documentation
        # ---------------------------------------------

        st.subheader("📚 Documentation Quality")

        st.write(
            data.get(
                "documentation_quality",
                "Not available"
            )
        )

        # ---------------------------------------------
        # Project Structure
        # ---------------------------------------------

        st.subheader("🏗️ Project Structure")

        st.write(
            data.get(
                "project_structure",
                "Not available"
            )
        )

        # ---------------------------------------------
        # Scalability
        # ---------------------------------------------

        st.subheader("📈 Scalability")

        st.write(
            data.get(
                "scalability",
                "Not available"
            )
        )

        # ---------------------------------------------
        # Maintainability
        # ---------------------------------------------

        st.subheader("🔧 Maintainability")

        st.write(
            data.get(
                "maintainability",
                "Not available"
            )
        )

        # ---------------------------------------------
        # Security
        # ---------------------------------------------

        st.subheader("🔐 Security Issues")

        security = data.get(
            "security_issues",
            []
        )

        if security:

            for issue in security:

                st.error(issue)

        else:

            st.success(
                "No security issues reported."
            )

        # ---------------------------------------------
        # Performance
        # ---------------------------------------------

        st.subheader("⚡ Performance Issues")

        performance = data.get(
            "performance_issues",
            []
        )

        if performance:

            for issue in performance:

                st.warning(issue)

        else:

            st.success(
                "No performance issues reported."
            )

        # ---------------------------------------------
        # Suggestions
        # ---------------------------------------------

        st.subheader("💡 Suggestions")

        suggestions = data.get(
            "suggestions",
            []
        )

        for suggestion in suggestions:

            st.info(
                suggestion
            )

        # ---------------------------------------------
        # Final Review
        # ---------------------------------------------

        st.subheader("📋 Final Review")

        st.write(
            data.get(
                "final_review",
                "Not available"
            )
        )

    else:

        st.info(
            "Analyze a repository to generate its review."
        )


# =========================================================
# TAB 4 — CHAT
# =========================================================

with tab4:

    st.header("💬 Chat with Repository")

    if not st.session_state.analysis:

        st.info(
            "Analyze a repository first before starting the chat."
        )

    else:

        # ---------------------------------------------
        # Display previous messages
        # ---------------------------------------------

        for message in st.session_state.chat_history:

            with st.chat_message(
                message["role"]
            ):

                st.write(
                    message["content"]
                )

        # ---------------------------------------------
        # Chat Input
        # ---------------------------------------------

        question = st.chat_input(
            "Ask something about the repository..."
        )

        if question:

            # Display user message

            st.session_state.chat_history.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            with st.chat_message("user"):

                st.write(question)

            try:

                with st.spinner(
                    "Searching repository..."
                ):

                    response = requests.post(
                        f"{API_URL}/chat",
                        json={
                            "query": question
                        },
                        timeout=120
                    )

                if response.status_code == 200:

                    result = response.json()

                    answer = result.get(
                        "response",
                        "No response received."
                    )

                    st.session_state.chat_history.append(
                        {
                            "role": "assistant",
                            "content": answer
                        }
                    )

                    with st.chat_message("assistant"):

                        st.write(answer)

                else:

                    try:

                        error = response.json()

                        st.error(
                            f"API Error: "
                            f"{error.get('detail', error)}"
                        )

                    except Exception:

                        st.error(
                            response.text
                        )

            except requests.exceptions.ConnectionError:

                st.error(
                    "❌ Could not connect to FastAPI."
                )

            except requests.exceptions.Timeout:

                st.error(
                    "⏱️ Chat request timed out."
                )

            except Exception as e:

                st.error(
                    f"Unexpected error: {str(e)}"
                )
