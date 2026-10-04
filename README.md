# Building Local LLMs for Private Workflows

Two fully offline, privacy-first AI projects built with **Ollama**, **LlamaIndex**, and open-source LLMs on Apple Silicon (MacBook Pro M1 Max). Nothing is sent to a cloud API, so sensitive documents and code never leave the machine.

| Project | What it does | Models |
|---|---|---|
| Internal policy chatbot (RAG) | Answers questions from an employee policy handbook using retrieval-augmented generation | Code Llama (answers), Mistral (embeddings) |
| Private coding assistant | On-device coding help from the terminal: write, debug, and translate code | DeepSeek-Coder 6.7B |

---

## Project 1: Internal policy chatbot (RAG)

A retrieval-augmented generation chatbot for a fictional company, SolaraTech. It answers employee questions from the company's policy documents instead of from the model's general knowledge.

**How it works** ([`solara_policy_chatbot.py`](solara_policy_chatbot.py))

1. Loads the policy documents from a `docs/` folder with LlamaIndex's `SimpleDirectoryReader`.
2. Generates embeddings locally with Mistral through Ollama.
3. Builds a `VectorStoreIndex` over the document chunks.
4. Runs a `condense_question` chat engine, which rewrites each follow-up into a standalone question, retrieves the relevant chunks, and answers with the local LLM.
5. Provides a simple command-line chat loop.

**Example questions**

- "What is the maximum PTO carryover?"
- "What happens if I lose a company laptop?"
- "How do I report a safety hazard?"

Sample policy document: [SolaraTech employee handbook](https://doc.clickup.com/9013904302/d/h/8cmagxe-53/ae1ae01503eecf7)

## Project 2: Private coding assistant

A fast coding assistant that runs entirely on-device with `DeepSeek-Coder 6.7B` through Ollama, prompted directly from the terminal. It needs no internet connection or cloud API.

**Example prompts**

- "Write a Python function that checks if a number is prime"
- "Can you help me debug this error?"
- "Translate this Python code into JavaScript"

---

## Running it

These projects run locally. Kaggle and other cloud notebooks can't run Ollama or local model inference.

1. Install [Ollama](https://ollama.com) and pull the models:

   ```bash
   ollama pull codellama
   ollama pull mistral
   ollama pull deepseek-coder:6.7b
   ```

2. Install the Python packages:

   ```bash
   pip install llama-index llama-index-llms-ollama llama-index-embeddings-ollama pypdf
   ```

3. Put your documents in a `docs/` folder and start the chatbot:

   ```bash
   python solara_policy_chatbot.py
   ```

4. For the coding assistant, run `ollama run deepseek-coder:6.7b`.

## Resources

- [Full project write-up (PDF)](Building%20Local%20LLMs.pdf)
- [View-only notebook on Kaggle](https://www.kaggle.com/code/elissaesterlein/building-local-llms-for-private-workflows)
