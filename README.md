# 🤖 AI Research Assistant

An AI-powered research assistant that generates structured research reports from a user's topic or question.

The application uses LangGraph to manage the AI workflow, Groq for LLM inference, Flask for the web application, and Render for cloud deployment.

## 📌 Project Overview

The AI Research Assistant helps users quickly generate organized research content.

A user enters a research topic through the web interface. The application sends the request through an AI workflow, processes the topic using an LLM, and returns a structured research report.

Example:

Input:
What is Generative AI?

Output:
A structured report containing sections such as title, introduction, key concepts, applications, and conclusion.

## 🏗️ Project Architecture

User
↓
HTML/CSS/JavaScript Interface
↓
Flask Application
↓
LangGraph Workflow
↓
AI Agent
↓
Groq LLM
↓
Generated Research Report
↓
Displayed in Web Interface

## 🛠️ Technologies Used

- Python
- Flask
- LangGraph
- LangChain
- Groq API
- HTML
- CSS
- JavaScript
- Git
- GitHub
- GitHub Actions
- Gunicorn
- Render

## 📂 Project Structure

ai_research_assistant/

├── app.py  
├── agents.py  
├── graph.py  
├── test_graph.py  
├── requirements.txt  
├── .gitignore  
├── .github/
│   └── workflows/
│       └── ci.yml  
├── templates/
│   └── index.html  
└── static/
    ├── style.css  
    └── script.js

## ⚙️ How It Works

1. The user enters a research topic in the web interface.
2. Flask receives the request.
3. The request is passed to the LangGraph workflow.
4. The AI agent processes the research topic.
5. Groq provides the LLM inference.
6. The generated report is returned to Flask.
7. The result is displayed to the user through the web interface.

## 🔄 CI/CD Pipeline

The project uses GitHub and GitHub Actions for Continuous Integration.

When code is pushed to the main branch:

1. GitHub receives the latest code.
2. GitHub Actions runs the CI workflow.
3. The workflow checks the Python project.
4. Render is connected to the GitHub repository.
5. New changes are automatically deployed to the hosted web application.

Pipeline:

Developer → GitHub → GitHub Actions → Render → Live Application

## 🚀 Deployment

The application is deployed as a web service on Render.

Build Command:

pip install -r requirements.txt

Start Command:

gunicorn app:app

Sensitive information such as API keys is stored using environment variables rather than being committed to GitHub.

## 📦 Main Dependencies

- Flask
- gunicorn
- langgraph
- langchain
- langchain-core
- langchain-groq
- python-dotenv
- requests

## 🔐 Environment Variables

The application uses environment variables for sensitive configuration such as the Groq API key.

Example:

GROQ_API_KEY=your_api_key

The `.env` file is excluded from GitHub using `.gitignore`.

## 🧪 Testing

The project includes `test_graph.py` for testing the AI workflow.

The CI workflow also helps validate the project whenever new changes are pushed to GitHub.

## ⚠️ Challenges Faced

During development and deployment, several issues were identified and resolved:

- Configuring the Python virtual environment
- Managing API keys securely
- Connecting the local project to GitHub
- Creating a GitHub Actions workflow
- Configuring Gunicorn for production deployment
- Resolving missing Python dependencies during deployment
- Configuring Render environment variables
- Successfully deploying and testing the application in a production environment

## 🎯 What I Learned

This project provided hands-on experience with:

- Building AI-powered Python applications
- Creating workflows using LangGraph
- Integrating an LLM using Groq
- Developing a Flask-based web interface
- Using Git and GitHub for version control
- Building a CI workflow with GitHub Actions
- Deploying Python applications using Render
- Managing production dependencies and environment variables
- Debugging deployment errors using application logs

## 👩‍💻 Author

Greeshma Sriram Sakhamuri