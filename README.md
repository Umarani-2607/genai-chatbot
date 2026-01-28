# GenAI Chatbot (AI Agent)

A production-style AI agent built with Python that demonstrates
prompt orchestration, conversational memory, cloud integration,
containerization, and CI/CD best practices.

---

## 🚀 Features

- Conversational AI agent with memory
- Structured prompt construction
- Amazon Bedrock (Nova Lite) integration
- Secure IAM-based access (no hardcoded credentials)
- Graceful fallback for local/Docker environments
- Dockerized application
- CI/CD pipeline using GitHub Actions

---

## 🧠 How It Works

1. User input is received through a CLI interface
2. Conversation history is stored in memory
3. A structured prompt is built using:
   - System instructions
   - Conversation context
   - Current user input
4. The agent:
   - Uses Amazon Bedrock if credentials are available
   - Falls back to a mock response if running locally or in CI
5. The response is returned to the user

---

## 🏗 Architecture

This project follows a simple agent-based architecture with clear separation
between conversation handling, memory, prompt construction, and AI response generation.
```
User (CLI Input)
↓
Chat Loop (app.py)
↓
Conversation Memory (in-memory list)
↓
Prompt Builder (system instructions + context)
↓
AI Response Generator
├─ Amazon Bedrock (Nova Lite) → when AWS credentials are available
└─ Mock Response → local, Docker, and CI environments
```

This diagram shows how user input flows through the agent and how
cloud dependencies are safely isolated.

