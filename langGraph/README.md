# 🤖 AI GitHub Repository Analyzer

An AI-powered GitHub Repository Analyzer built using **LangGraph**, **LangChain**, **Mistral AI**, **FAISS**, and **Streamlit**. Simply provide a public GitHub repository URL, and the application clones the repository, indexes its source code using Retrieval-Augmented Generation (RAG), and generates an AI-powered analysis including a project summary, architecture overview, and code review.

---

## 🚀 Features

* 🔗 Clone any public GitHub repository
* 📂 Load source code and documentation files automatically
* 🧩 Split code into semantic chunks
* 🧠 Generate embeddings using Mistral AI
* 🔍 Store embeddings in a FAISS vector database
* 🤖 Analyze repositories using LangGraph agents
* 📄 Generate an AI-powered project summary
* 🏗 Analyze repository architecture
* 🔎 Perform an automated code review
* 📥 Export the analysis as a report
* 🌐 Interactive Streamlit web interface

---

## 🛠 Tech Stack

### AI & LLM

* LangChain
* LangGraph
* Mistral AI
* Mistral Embeddings

### Vector Database

* FAISS

### Frontend

* Streamlit

### Language

* Python

---

## 📁 Project Structure

```text
langGraph/
│
├── app.py                 # Streamlit UI
├── agentic.py             # LangGraph workflow
├── db.py                  # File loading, chunking, FAISS database
├── git_clone.py           # Clone GitHub repositories
├── report_maker.py        # Generate analysis report
├── repositories/          # Cloned repositories
├── report.txt             # Generated report
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. Enter a public GitHub repository URL.
2. Clone the repository locally.
3. Load supported source code and documentation files.
4. Split files into chunks using a Recursive Character Text Splitter.
5. Generate embeddings with Mistral AI.
6. Store embeddings in a FAISS vector database.
7. Retrieve relevant code snippets using RAG.
8. Execute three LangGraph agents in parallel:

   * Summary Agent
   * Architecture Agent
   * Code Review Agent
9. Display the results in the Streamlit UI.
10. Export the complete analysis as a text report.

---

## 🤖 LangGraph Workflow

```text
                START
                   │
        ┌──────────┼──────────┐
        │          │          │
        ▼          ▼          ▼
   Summary   Architecture   Review
        │          │          │
        └──────────┼──────────┘
                   ▼
                  END
```

Each agent retrieves relevant repository context from the FAISS vector store before generating its analysis.

---

## 📄 AI Agents

### 📄 Summary Agent

Generates:

* Project name
* Purpose
* Features
* Programming language
* Frameworks
* Folder structure overview
* Target users

---

### 🏗 Architecture Agent

Analyzes:

* Overall architecture
* Modules
* Responsibilities
* Data flow
* Dependencies
* Entry point
* Database usage
* APIs
* AI components
* Improvement suggestions

---

### 🔍 Code Review Agent

Reviews:

* Code quality
* Readability
* Naming conventions
* Project structure
* Error handling
* Security
* Performance
* Code duplication
* Documentation
* Best practices

---

## 📂 Supported File Types

The analyzer currently indexes:

* `.py`
* `.js`
* `.ts`
* `.tsx`
* `.jsx`
* `.html`
* `.css`
* `.json`
* `.yaml`
* `.yml`
* `.toml`
* `.ini`
* `.sql`
* `.md`
* `.txt`
* `.ipynb`
* `.env.example`

---

## 📦 Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open the displayed local URL in your browser.

---

## 📋 Example Workflow

1. Paste a GitHub repository URL.
2. Click **Analyze Repository**.
3. Wait for cloning and indexing.
4. View:

   * Project Summary
   * Architecture Analysis
   * Code Review
5. Download the generated report.

---

## 📊 Output

The application generates:

* AI Project Summary
* Architecture Report
* Code Review Report
* Downloadable text report

---

## 🔮 Future Improvements

* Support private GitHub repositories
* Repository chat assistant
* Dependency visualization
* Project diagrams
* Multi-LLM support
* PDF report generation
* Repository comparison
* Commit history analysis
* Pull request review
* Code quality scoring
* Docker support
* Deployment with FastAPI

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your fork.
5. Open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Anuj Shrestha**

If you found this project useful, consider giving it a ⭐ on GitHub.
