# 📂 AI GitHub Repository Analyzer

An AI-powered GitHub Repository Analyzer built with **LangChain**, **RAG (Retrieval-Augmented Generation)**, **ChromaDB**, **Mistral AI**, **Groq**, and **Streamlit**.

The application clones any public GitHub repository, indexes its source code into a vector database, and allows users to:

- 🔍 Analyze repository structure
- 📝 Generate project summaries
- ⭐ Review code quality
- 💬 Chat with the repository using RAG
- 📄 Export an analysis report

---

## 🚀 Features

- Clone any public GitHub repository
- Automatically load source code files
- Split code into semantic chunks
- Store embeddings in ChromaDB
- AI-powered repository analysis
- AI-generated project summary
- AI code review with recommendations
- Repository chat assistant
- Downloadable report generation
- Streamlit Web Interface
- Progress bar for analysis pipeline
- README viewer inside the application

---

## 🏗️ Architecture

```
                GitHub Repository URL
                         │
                         ▼
                Clone Repository
                         │
                         ▼
                 Load Repository Files
                         │
                         ▼
                  Chunk Source Code
                         │
                         ▼
              Mistral Embedding Model
                         │
                         ▼
                     ChromaDB
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
    Repository      Project        Project
     Analysis       Summary         Review
          │
          ▼
      Report Generator
          │
          ▼
     Repository Chat (RAG)
```

---

# 📁 Project Structure

```
Github_Analyzer/
│
├── repositories/           # Cloned repositories
├── repo_db/                # Chroma Vector Database
│
├── rag_engine.py           # Main RAG pipeline
├── git_clone.py            # Clone GitHub repository
├── db.py                   # Build Chroma vector database
├── llms.py                 # LLM prompts & structured outputs
├── report_maker.py         # Report generation
│
├── report.txt              # Generated report
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Tech Stack

## Languages

- Python

## LLMs

- Mistral Large
- Llama 3.3 70B (Groq)

## Frameworks

- LangChain
- Streamlit

## Vector Database

- ChromaDB

## Embedding Model

- Mistral Embed

## Other Libraries

- GitPython / subprocess
- python-dotenv
- Pydantic

---

# 📦 Installation

Clone this repository

```bash
git clone https://github.com/AnujrajShrestha/github_repo_analyser

cd github_repo_analyser
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
MISTRAL_API_KEY=your_mistral_api_key

GROQ_API_KEY=your_groq_api_key
```

---

# 🧠 Analysis Pipeline

```
Clone Repository
        │
        ▼
Load Repository Files
        │
        ▼
Create Chunks
        │
        ▼
Generate Embeddings
        │
        ▼
Store in ChromaDB
        │
        ▼
Repository Analysis
        │
        ▼
Project Summary
        │
        ▼
Repository Review
        │
        ▼
Generate Report
        │
        ▼
Repository Chat
```

---

# 📊 AI Agents

## 1. Repository Analysis Agent

Extracts:

- Project Name
- Languages
- Frameworks
- Dependencies
- Folder Structure
- Entry Points
- Important Files

---

## 2. Project Summary Agent

Generates:

- Purpose
- Category
- Tech Stack
- Features
- Project Overview

---

## 3. Repository Review Agent

Evaluates:

- Code Quality
- Documentation
- Maintainability
- Scalability
- Security
- Performance

Provides an overall project score and actionable suggestions.

---

## 4. Repository Chat Assistant

Uses Retrieval-Augmented Generation (RAG) to answer questions based only on the indexed repository content.

Example questions:

- Explain this project.
- What does `db.py` do?
- Which frameworks are used?
- How is authentication implemented?
- Where is the main entry point?
- Explain the folder structure.
- Summarize the README.

---

# 📄 Report Generation

The application generates a report (`report.txt`) containing:

- Repository Analysis
- Project Summary
- Project Review

---


# 📸 Workflow

```
Enter Repository URL
        │
        ▼
Analyze Repository
        │
        ▼
View Analysis
        │
        ▼
View Summary
        │
        ▼
View Review
        │
        ▼
Read README
        │
        ▼
Chat with Repository
        │
        ▼
Download Report
```

---

# 🎯 Future Improvements

- GitHub API integration (Stars, Forks, License, Issues)
- Repository visualization
- Dependency graph
- File explorer
- Multi-repository comparison
- Local folder analysis
- Docker support
- PDF report generation
- Code search
- Repository bookmarking
- Incremental indexing
- Syntax-highlighted source viewer

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Anuj Shrestha**

GitHub: https://github.com/AnujrajShrestha

---

⭐ If you found this project useful, consider giving it a star on GitHub!