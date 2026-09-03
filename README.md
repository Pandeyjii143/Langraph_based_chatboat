# LangGraph Chatbot

A conversational AI chatbot built using **LangGraph**, **LangChain**, **OpenAI**, and **Streamlit**. The application supports real-time response streaming, persistent conversation memory using SQLite, multiple chat threads, and conversation history management.

## Features

### Real-Time Streaming

* Streams AI responses token-by-token for a smooth chat experience.
* Uses LangGraph streaming capabilities integrated with Streamlit.

### Persistent Memory

* Stores conversation state using SQLite-based checkpointing.
* Chat history remains available even after application restarts.

### Multi-Thread Conversations

* Create multiple chat sessions.
* Each conversation receives a unique thread ID.
* Easily switch between previous conversations.

### Conversation History

* View and revisit past chats from the sidebar.
* Load previous messages instantly.

### Streamlit User Interface

* Clean and responsive chat interface.
* Sidebar for chat management.
* One-click "New Chat" functionality.

### LangGraph Workflow

* Built using LangGraph's StateGraph architecture.
* Supports stateful conversation flows.
* Easy to extend with tools, agents, and workflows.

---

## Tech Stack

* Python
* LangGraph
* LangChain
* OpenAI API
* Streamlit
* SQLite
* Pydantic

---

## Project Structure

```text
langraph_chatboat/
│
├── streamlit_frontend.py      # Streamlit UI
├── langraph_backend.py        # LangGraph workflow
├── .env                       # API keys
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd langraph_chatboat
```

### Create Virtual Environment

```bash
python -m venv myenv
```

### Activate Environment

Windows PowerShell:

```powershell
.\myenv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## Run the Application

```bash
streamlit run streamlit_frontend.py
```

Application will be available at:

```text
http://localhost:8501
```

---

## How It Works

1. User enters a message in Streamlit.
2. Message is sent to LangGraph.
3. LangGraph invokes the LLM.
4. Response is streamed back to the UI.
5. Conversation state is saved in SQLite.
6. Previous conversations can be reopened using the sidebar.

---

## Future Improvements

* Chat title generation using LLM
* Conversation search
* File upload support
* RAG integration
* Tool calling and agents
* Authentication and user accounts
* Cloud deployment

---

## Learning Objectives

This project demonstrates:

* LangGraph StateGraph workflows
* Persistent memory using checkpointing
* Streaming LLM responses
* Streamlit chat interfaces
* Multi-session conversation management
* Production-ready chatbot architecture

---

## Author

**Ravikishan Pandey**

Engineering Student | AI & Full-Stack Development Enthusiast
