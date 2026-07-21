from pydantic import BaseModel, Field
from typing import List
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from langchain_groq import ChatGroq

llm_mistral= ChatMistralAI(
    model="mistral-large-latest",
    temperature=0
)

llm_groq= ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.5,
)

class RepositoryAnalysisOutput(BaseModel):
    """Repository metadata."""

    status: str = Field(
        description="Status of repository analysis."
    )

    project_name: str = Field(
        description="Repository or project name."
    )

    root_directory: str = Field(
        description="Root directory of the repository."
    )

    total_files: int = Field(
        description="Total number of files."
    )

    total_folders: int = Field(
        description="Total number of folders."
    )

    folder_structure: List[str] = Field(
        description="Folder tree of the repository."
    )

    programming_languages: List[str] = Field(
        description="Languages detected in the repository."
    )

    frameworks: List[str] = Field(
        description="Frameworks used in the project."
    )

    dependencies: List[str] = Field(
        description="Libraries/packages used."
    )

    entry_points: List[str] = Field(
        description="Possible application entry files."
    )

    important_files: List[str] = Field(
        description="README, requirements.txt, package.json, Dockerfile, etc."
    )

    project_type: str = Field(
        description="Detected project type."
    )
    
analysis_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert Software Architect and Repository Analyzer.

Your task is to analyze the entire GitHub repository.

Carefully inspect every folder and file to determine:

- Project name
- Root directory
- Total files
- Total folders
- Folder structure
- Programming languages
- Frameworks
- Libraries and dependencies
- Entry point files
- Important configuration files
- Project type

Only provide factual information obtained from the repository.

Return the response following the RepositoryAnalysisOutput schema.
"""
    ),
    (
        "human",
        "{query}"
        "Repository Context:{context}"

    )
])
    
class ProjectSummaryOutput(BaseModel):
    """Project summary."""

    status: str = Field("Status of summarizaton.")

    project_name: str= Field(description="generate project name")

    purpose: str = Field(
        description="Main purpose of the project."
    )

    project_category: str = Field(
        description="Web app, ML, AI, API, CLI, etc."
    )

    key_features: List[str] = Field(
        description="Major features."
    )

    tech_stack: List[str] = Field(
        description="Technologies used."
    )

    summary: str = Field(
        description="Short project summary."
    )
    
summary_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an experienced Software Engineer.

Summarize the entire GitHub repository.

Your summary should include:

- Project name
- Main purpose
- Project category
- Key features
- Technologies used
- Short project overview

Keep the summary concise, professional, and easy to understand.

Return the response following the ProjectSummaryOutput schema.
"""
    ),
    (
        "human",
        "{query}"
        "Repository Context:{context}"
    )
])
    
class ProjectReviewOutput(BaseModel):
    """Repository review."""

    status: str= Field("Status of repository review.")

    overall_score: float = Field(
        description="Overall score out of 10."
    )

    strengths: List[str] = Field(
        description="Strong points of the project."
    )

    weaknesses: List[str] = Field(
        description="Weaknesses found."
    )

    code_quality: str= Field(description="Code quality")

    documentation_quality: str= Field(description="Documentation quality")

    project_structure: str= Field(description= "project structure")

    scalability: str= Field(description="Scalabe ot not")

    maintainability: str= Field(description="maintance required or not")

    security_issues: List[str]= Field(description="Find security issues")

    performance_issues: List[str]= Field(description="Find proformance issues")

    suggestions: List[str]= Field(description="Give suggestions")

    final_review: str= Field("Final review of project")
    
review_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a Senior Software Reviewer.

Review the complete GitHub repository.

Evaluate:

- Code quality
- Documentation
- Folder structure
- Maintainability
- Scalability
- Security
- Performance

Highlight:

- Strengths
- Weaknesses
- Possible security issues
- Performance bottlenecks
- Improvement suggestions

Assign an overall score out of 10.

Be constructive and provide actionable recommendations.

Return the response following the ProjectReviewOutput schema.
"""
    ),
    (
        "human",
        "{query}"
        "Repository Context:{context}"
    )
])
    
class ProjectChatOutput(BaseModel):
    """Answer user questions about repository."""

    response: str= Field(description="llm response")
    
chat_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an AI GitHub Repository Assistant.

Answer the user's question using ONLY the retrieved repository context.

Rules:

- Do not invent information.
- If the answer cannot be found in the retrieved files, clearly state that.
- Mention the relevant files used to answer.
- Be technically accurate.
- Explain code in simple language unless the user requests detailed technical explanations.

Return the response following the ProjectChatOutput schema.
"""
    ), ("placeholder", "{history}"),
    (
        "human",
        """
Repository Context:

{context}

User Question:

{query}
"""
    )
])

analysis_chain = analysis_prompt | llm_groq.with_structured_output(RepositoryAnalysisOutput)

summary_chain = summary_prompt | llm_groq.with_structured_output(ProjectSummaryOutput)

review_chain = review_prompt | llm_mistral.with_structured_output(ProjectReviewOutput)

chat_chain = chat_prompt | llm_mistral.with_structured_output(ProjectChatOutput)