# Architecture Overview

This project implements a conversational GenAI agent with a clear separation
between conversation handling, prompt construction, and response generation.

The design focuses on reliability, security, and cloud-safe execution.

---

## High-Level Flow

User Input  
→ Chat Loop  
→ Conversation Memory  
→ Prompt Builder  
→ AI Response Generator  

---

## AI Response Generation

The agent supports two execution modes:

### 1. Cloud Mode (Amazon Bedrock)
- Uses Amazon Bedrock (Nova Lite) for LLM inference
- Accessed securely via IAM roles
- No credentials are hardcoded in the application

### 2. Local / CI Mode (Mock Response)
- Used when cloud credentials are not available
- Ensures the application runs safely in local and CI environments
- Avoids unnecessary cloud dependencies during testing

---

## Key Design Goals

- Cloud-agnostic execution
- Secure credential handling
- Predictable behavior in CI/CD pipelines
- Clear separation of concerns
