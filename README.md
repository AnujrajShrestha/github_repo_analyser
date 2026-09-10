# 🤖 GitHub Repository Analyzer

An AI-powered application that analyzes GitHub repositories and helps developers understand unfamiliar codebases.

The application clones a repository, processes its source files, creates a vector database using **ChromaDB**, retrieves relevant context with **RAG**, and uses LLMs to generate a structured **analysis, summary, code review, and repository-aware answers**.

## ✨ Features

### 🔍 Repository Analysis

Analyze the technical structure of a GitHub repository, including:

* Project name
* Root directory
* Total files and folders
* Folder structure
* Programming languages
* Frameworks
* Dependencies
* Entry points
* Important files
* Project type

### 📝 AI Project Summary

Automatically generate:

* Project purpose
* Project category
* Key features
* Technology stack
* Project overview

### ⭐ AI Code Review

Get an AI-powered review containing:

* Overall score
* Strengths
* Weaknesses
* Code quality
* Documentation quality
* Project structure
* Scalability
* Maintainability
* Security issues
* Performance issues
* Improvement suggestions
* Final review

### 💬 Repository Chat

Ask questions about the analyzed repository using a RAG-based AI assistant.

Example questions:

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

The assistant retrieves relevant repository context before generating an answer.

---

## 🧠 How It Works

The application uses a **Retrieval-Augmented Generation (RAG)** pipeline.

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
             ┌───────────┼───────────┐
             ▼           ▼           ▼
          Analysis     Summary      Review
             │           │           │
             └───────────┼───────────┘
                         ▼
                    FastAPI API
                         │
                         ▼
                    React Frontend
```

The repository pipeline performs:

```text
Clone
  ↓
Load Files
  ↓
Create Chunks
  ↓
Generate Embeddings
  ↓
Create Vector Database
  ↓
Retrieve Context
  ↓
AI Analysis
  ↓
Generate Summary
  ↓
AI Review
  ↓
Return Results
```

The backend also provides repository-aware chat through the retriever and LLM.

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn
* Pydantic

### AI / LLM

* LangChain
* Groq
* Mistral AI
* Groq-hosted LLM
* Mistral LLM
* Mistral Embeddings

### RAG

* ChromaDB
* Mistral Embeddings
* Recursive Character Text Splitter
* LangChain Retrievers

### Repository Processing

* Git
* GitPython / Git CLI
* LangChain DirectoryLoader
* TextLoader

### Frontend

* React
* Vite
* Tailwind CSS
* JavaScript
* Lucide React

---

## 📁 Project Structure

```text
github_repo_analyser/
│
├── RAG_engine/
│   ├── rag_engine.py
│   ├── llms.py
│   ├── db.py
│   ├── git_clone.py
│   └── ...
│
├── backend/
│   └── main.py
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── services/
│   │       └── api.js
│   │
│   ├── package.json
│   └── ...
│
├── repositories/
├── repo_db/
├── requirements.txt
├── .gitignore
└── README.md
```

The main backend is implemented in `backend/main.py`, while the RAG and LLM components are organized under `RAG_engine/`.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/AnujrajShrestha/github_repo_analyser.git
```

```bash
cd github_repo_analyser
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key
GROQ_API_KEY=your_groq_api_key
```

### API Keys

**Mistral AI** is used for:

* LLM capabilities
* Repository embeddings

**Groq** is used for:

* Repository analysis
* Project summarization
* AI-powered review

Never commit your `.env` file to GitHub.

---

## 🚀 Running the Backend

From the project root:

```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

> **Note:** The current development frontend uses port `8000` for the FastAPI API. If you change the backend port, update the frontend API configuration accordingly.

---

## 💻 Running the Frontend

Navigate to the frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the Vite development server:

```bash
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173
```

---

## 🔌 API Endpoints

### Health Check

```http
GET /
```

Example response:

```json
{
  "message": "GitHub Repository Analyzer API is running"
}
```

### Analyze Repository

```http
POST /analyze
```

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

### Repository Chat

```http
POST /chat
```

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

The FastAPI backend exposes the health check, repository analysis, and chat endpoints.

---

## 🔄 Example Workflow

1. Start the FastAPI backend.
2. Start the React frontend.
3. Open the frontend in your browser.
4. Enter a public GitHub repository URL.
5. Click **Analyze**.
6. The backend clones and processes the repository.
7. Repository files are split into chunks.
8. Mistral generates embeddings.
9. ChromaDB stores the vector representations.
10. Relevant context is retrieved.
11. The LLM generates the analysis, summary, and review.
12. Results are returned to the frontend.
13. You can ask questions about the repository through the AI chat.

---

## ⚠️ Current Limitations

* Only public GitHub repositories are currently supported.
* Large repositories can take longer to process.
* Embedding and LLM operations require API usage.
* The current ChromaDB implementation uses a shared database directory.
* Chat history is maintained in backend memory.
* Concurrent repository analysis may cause database conflicts.
* Authentication is not implemented yet.
* Background job processing is not implemented yet.

---

## 🔮 Future Improvements

* GitHub OAuth authentication
* Private repository support
* Repository-specific ChromaDB collections
* Multi-user support
* Background analysis jobs
* Real-time analysis progress
* Repository history analysis
* Downloadable PDF reports
* Markdown report generation
* Automatic README generation
* Advanced code-quality scoring
* Dependency vulnerability detection

---

## 🎯 Project Goal

The goal of this project is to make **understanding an unfamiliar GitHub repository faster and easier**.

Instead of manually exploring hundreds of files, developers can provide a repository URL and receive an AI-generated overview of its architecture, technologies, dependencies, strengths, weaknesses, and potential improvements.

---

## 👨‍💻 Author

**Anuj Shrestha**

GitHub: [AnujrajShrestha](https://github.com/AnujrajShrestha)

---
This project cannot deployed bacause author don't have money todeployed this heavy RAG application. 😭😭😭
But you can the appliction interface screenshots on interfaces folder. 😊

---

## 📄 License

This project is intended for educational and development purposes.
