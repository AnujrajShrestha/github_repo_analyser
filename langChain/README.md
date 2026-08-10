# 🤖 GitHub Repository Analyzer

An AI-powered GitHub Repository Analyzer that automatically clones, indexes, analyzes, summarizes, reviews, and answers questions about GitHub repositories.

The project combines **FastAPI, LangChain, RAG, ChromaDB, Groq, Mistral AI, and a vanilla HTML/CSS/JavaScript frontend** to provide an interactive repository analysis platform.

---

## ✨ Features

### 📊 Repository Analysis

Analyze the structure and technical details of a GitHub repository.

The analyzer detects:

* Project name
* Root directory
* Total files
* Total folders
* Folder structure
* Programming languages
* Frameworks
* Dependencies
* Entry points
* Important configuration files
* Project type

---

### 📝 Project Summary

Automatically generates a professional project summary containing:

* Project purpose
* Project category
* Key features
* Technology stack
* Project overview

---

### ⭐ AI Code Review

The AI reviews the repository and provides:

* Overall score out of 10
* Strengths
* Weaknesses
* Code quality analysis
* Documentation quality
* Project structure evaluation
* Scalability analysis
* Maintainability analysis
* Security issues
* Performance issues
* Improvement suggestions
* Final review

---

### 💬 Repository Chat

Ask questions about the analyzed repository using a RAG-based AI assistant.

Examples:

```text
What is the purpose of this project?

What technologies are used?

Where is the application entry point?

Explain the authentication system.

Which database does this project use?

How can I run this project?

Are there any security issues?

How can I improve the project structure?
```

The assistant retrieves relevant code and documentation from the repository before generating an answer.

---

## 🧠 How It Works

The application follows a Retrieval-Augmented Generation architecture.

```text
                  GitHub Repository
                         │
                         ▼
                    Git Clone
                         │
                         ▼
                  Repository Files
                         │
                         ▼
                  Document Loader
                         │
                         ▼
                  Text Chunking
                         │
                         ▼
               Mistral Embeddings
                         │
                         ▼
                    ChromaDB
                         │
                         ▼
                    Retriever
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
           Analysis   Summary     Review
              │          │          │
              └──────────┼──────────┘
                         ▼
                    FastAPI API
                         │
                         ▼
                  HTML/CSS/JS UI
```

For repository chat:

```text
User Question
      │
      ▼
FastAPI /chat
      │
      ▼
ChromaDB Retriever
      │
      ▼
Relevant Repository Chunks
      │
      ▼
Mistral LLM
      │
      ▼
AI Response
      │
      ▼
Frontend
```

---

# 🛠️ Tech Stack

## Backend

* Python
* FastAPI
* Uvicorn
* Pydantic

## AI / LLM

* LangChain
* Groq
* Mistral AI
* `llama-3.3-70b-versatile`
* `mistral-large-latest`
* `mistral-embed`

## RAG

* ChromaDB
* Mistral Embeddings
* Recursive Character Text Splitter
* LangChain Retrievers

## Repository Processing

* Git
* GitPython / Git CLI
* LangChain DirectoryLoader
* TextLoader

## Frontend

* HTML5
* CSS3
* JavaScript
* Fetch API

---

# 📁 Project Structure

```text
github-repository-analyzer/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── repositories/
│
├── repo_db/
│
├── main.py
├── git_clone.py
├── db.py
├── llms.py
├── rag_engine.py
├── report_maker.py
│
├── report.txt
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🔍 File Responsibilities

### `main.py`

FastAPI application.

Provides API endpoints:

```text
GET  /
POST /analyze
POST /chat
```

It connects the frontend with the AI/RAG pipeline.

---

### `git_clone.py`

Responsible for cloning GitHub repositories.

```python
clone_repo(url)
```

Repositories are stored inside:

```text
repositories/
```

---

### `db.py`

Responsible for:

1. Loading repository files
2. Splitting documents into chunks
3. Generating embeddings
4. Creating ChromaDB

Main functions:

```python
loadfiles()
create_chunks()
create_db()
run_db()
```

---

### `llms.py`

Contains:

* LLM configuration
* Pydantic output schemas
* Prompt templates
* Analysis chain
* Summary chain
* Review chain
* Chat chain

Example:

```python
analysis_chain
summary_chain
review_chain
chat_chain
```

---

### `rag_engine.py`

Contains the main RAG pipeline.

The primary function is:

```python
run_pipeline()
```

It performs:

```text
Clone
  ↓
Load Files
  ↓
Create Chunks
  ↓
Create Vector Database
  ↓
Retrieve Context
  ↓
Analysis
  ↓
Summary
  ↓
Review
  ↓
Generate Report
```

It also contains the repository retrieval function:

```python
load_context()
```

and the repository chat functionality.

---

### `report_maker.py`

Generates:

```text
report.txt
```

containing:

* Analysis
* Summary
* Review

---

### `frontend/index.html`

Main user interface.

Contains:

* Repository URL input
* Analysis dashboard
* Summary section
* Review section
* AI chat interface

---

### `frontend/style.css`

Provides the frontend styling and responsive layout.

---

### `frontend/script.js`

Connects the frontend to FastAPI using the JavaScript Fetch API.

Example:

```javascript
fetch("http://127.0.0.1:6600/analyze", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        url: repoUrl
    })
});
```

---

# ⚙️ Installation

## 1. Clone the project

```bash
git clone https://github.com/your-username/github-repository-analyzer.git
```

Move into the project:

```bash
cd github-repository-analyzer
```

---

## 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_mistral_api_key
GROQ_API_KEY=your_groq_api_key
```

Do not commit `.env` to GitHub.

Add this to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
repositories/
repo_db/
*.pyc
```

---

# 🔑 API Keys

This project requires API access for:

### Mistral AI

Used for:

* Mistral LLM
* Mistral embeddings

### Groq

Used for:

* Repository analysis
* Project summarization

Make sure the required API keys are available in your environment before starting the backend.

---

# 🚀 Running the Application

The project has two components:

```text
Frontend
   +
FastAPI Backend
```

Both need to be running.

---

## Start FastAPI

Run:

```bash
uvicorn main:app --host 0.0.0.0 --port 6600 --reload
```

The API will run at:

```text
http://127.0.0.1:6600
```

FastAPI Swagger documentation:

```text
http://127.0.0.1:6600/docs
```

---

## Start Frontend

Navigate to the frontend directory:

```bash
cd frontend
```

Run Python's development HTTP server:

```bash
python -m http.server 5500
```

Open:

```text
http://127.0.0.1:5500
```

---

# 🔌 API Endpoints

## Health Check

### `GET /`

Checks whether the backend is running.

Example response:

```json
{
    "message": "GitHub Repository Analyzer API is running"
}
```

---

## Analyze Repository

### `POST /analyze`

Analyzes a GitHub repository.

Request:

```json
{
    "url": "https://github.com/user/project"
}
```

Response:

```json
{
    "status": "success",
    "repository": "https://github.com/user/project",
    "analysis": {},
    "summary": {},
    "review": {}
}
```

---

## Chat

### `POST /chat`

Ask a question about the repository.

Request:

```json
{
    "query": "What technologies are used in this project?"
}
```

Response:

```json
{
    "status": "success",
    "question": "What technologies are used in this project?",
    "response": "..."
}
```

---

# 🧪 Example Workflow

1. Start FastAPI.

```bash
uvicorn main:app --host 0.0.0.0 --port 6600 --reload
```

2. Start the frontend.

```bash
cd frontend
python -m http.server 5500
```

3. Open:

```text
http://127.0.0.1:5500
```

4. Enter a public GitHub repository URL.

Example:

```text
https://github.com/user/project
```

5. Click:

```text
Analyze Repository
```

6. The backend:

```text
Clones repository
       ↓
Loads source files
       ↓
Creates chunks
       ↓
Generates embeddings
       ↓
Stores vectors in ChromaDB
       ↓
Retrieves repository context
       ↓
Runs AI analysis
       ↓
Generates summary
       ↓
Reviews project
       ↓
Returns JSON
```

7. The frontend displays the results.

8. Use the **Chat** section to ask questions about the repository.

---

# 🔐 CORS

FastAPI is configured to allow requests from the frontend.

Example:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

For production, replace:

```python
allow_origins=["*"]
```

with your actual frontend domain.

---

# ⚠️ Current Limitations

The current version has some limitations:

* Only public GitHub repositories are supported.
* Large repositories can take significant time to process.
* Repository embeddings require API usage.
* The current ChromaDB implementation uses a shared `repo_db` directory.
* Chat history is currently maintained in backend memory.
* Concurrent repository analysis can cause database conflicts.
* Authentication is not currently implemented.
* Background job processing is not yet implemented.

---

# 🔮 Future Improvements

Possible future features:

* [ ] GitHub OAuth authentication
* [ ] Private repository support
* [ ] Repository-specific ChromaDB collections
* [ ] Multiple simultaneous users
* [ ] Background analysis jobs
* [ ] Analysis progress tracking
* [ ] Repository history
* [ ] Downloadable PDF reports
* [ ] Markdown report generation
* [ ] GitHub README generation
* [ ] Code quality scoring
* [ ] Dependency vulnerability detection
* [ ] Architecture diagram generation
* [ ] GitHub commit analysis
* [ ] Pull request review
* [ ] Automatic README generation
* [ ] Docker deployment
* [ ] Cloud deployment
* [ ] User authentication
* [ ] Persistent chat history

---

# 🏗️ Architecture

```text
                         ┌──────────────────┐
                         │     Browser      │
                         │ HTML/CSS/JS      │
                         └────────┬─────────┘
                                  │
                             HTTP / JSON
                                  │
                                  ▼
                         ┌──────────────────┐
                         │     FastAPI      │
                         │                  │
                         │ /analyze         │
                         │ /chat            │
                         └────────┬─────────┘
                                  │
                   ┌──────────────┼──────────────┐
                   │              │              │
                   ▼              ▼              ▼
              Git Clone       ChromaDB       LLM Chains
                   │              │              │
                   ▼              ▼         ┌────┴────┐
             Repository       Retriever      │         │
               Files              │         Groq    Mistral
                                   │
                                   ▼
                              AI Response
                                   │
                                   ▼
                                FastAPI
                                   │
                                   ▼
                                Browser
```

---

# 📚 RAG Pipeline

The repository is transformed into searchable knowledge using the following pipeline:

```text
Repository
    ↓
File Loading
    ↓
Document Extraction
    ↓
RecursiveCharacterTextSplitter
    ↓
Text Chunks
    ↓
MistralAIEmbeddings
    ↓
ChromaDB
    ↓
MMR Retriever
    ↓
Relevant Context
    ↓
LLM
    ↓
Structured Response
```

The retriever currently uses:

```python
search_type="mmr"
```

with:

```python
k=8
fetch_k=12
lambda_mult=0.5
```

---

# 📄 Generated Report

After repository analysis, the system generates:

```text
report.txt
```

The report contains:

```text
Step 1 - Analysis
Step 2 - Summary
Step 3 - Review
```

---

# 🎯 Project Goal

The goal of this project is to make understanding unfamiliar GitHub repositories faster and easier.

Instead of manually reading hundreds of files, developers can provide a repository URL and allow the AI system to:

```text
Understand
Analyze
Summarize
Review
Answer questions
```

about the project using the actual repository contents as context.

---

# 👨‍💻 Author

**Anuj Shrestha**

GitHub:

```text
https://github.com/AnujrajShrestha
```

---

# ⭐ If You Like This Project

If this project helped you understand RAG, LangChain, FastAPI, or AI-powered developer tools, consider giving the repository a ⭐ on GitHub.

---

## 📜 License

This project is intended for educational and portfolio purposes.
