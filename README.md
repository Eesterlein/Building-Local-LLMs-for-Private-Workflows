# Building-Local-LLMs-for-Private-Workflows
This repo showcases two fully offline, privacy-first AI projects built using **Ollama**, **LlamaIndex**, and open-source LLMs on a MacBook Pro M1 Max.
# 🤖 Building Local LLMs for Private Workflows

This repo showcases two fully offline, privacy-first AI projects built using **Ollama**, **LlamaIndex**, and open-source LLMs on a MacBook Pro M1 Max.

---

## 🚀 Project 1: Private Coding Copilot

A fast, private coding assistant that runs entirely on-device using:

- 🧠 `DeepSeek-Coder 6.7B` via Ollama
- ⌨️ Prompted directly through Terminal
- ⚡ No internet connection or cloud API required

**Sample Prompts:**
- “Write a Python function that checks if a number is prime”
- “Can you help me debug this error?”
- “Translate this Python code into JavaScript”

📄 Project notes: [`coding-copilot/instructions.md`](coding-copilot/instructions.md)

---

## 🗂️ Project 2: Internal Company Policy Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that answers questions based on internal policy docs using:

- 🧠 Ollama + Mistral for local LLM + embeddings
- 📚 LlamaIndex for document search
- 💻 Python CLI for user interaction

**Test Prompts:**
- “What is the maximum PTO carryover?”
- “What happens if I lose a company laptop?”
- “How do I report a safety hazard?”

📜 Code: [`chatbot/chatbot.py`](chatbot/chatbot.py)  
📄 Sample document: [`chatbot/docs/solara_employee_handbook.txt`](chatbot/docs/solara_employee_handbook.txt)

---

## 📎 Resources

- 🧾 Full project write-up: [Google Doc](https://docs.google.com/document/d/1cC-siprH2b46xzyXPyNrosrfjkvE-rO7g74NUf38iEc/edit?usp=sharing)
- 🧪 View-only notebook on Kaggle: [Kaggle: Building Local LLMs](https://www.kaggle.com/code/elissaesterlein/building-local-llms-for-private-workflows)

---

⚠️ These projects are designed to run locally. Kaggle or cloud environments do not support Ollama or local model inference.

---

## 🔧 Requirements

```txt
ollama
llama-index
llama-index-llms-ollama
llama-index-embeddings-ollama
pypdf
