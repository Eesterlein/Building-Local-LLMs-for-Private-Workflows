from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

# Set up local LLM and embedding model
llm = Ollama(model="codellama")  # You can swap in "deepseek-coder" if you want
embed_model = OllamaEmbedding(model_name="mistral")  # Works well for embedding

Settings.llm = llm
Settings.embed_model = embed_model

# Load your documents
documents = SimpleDirectoryReader("docs").load_data()

# Create an index from documents
index = VectorStoreIndex.from_documents(documents)

# Create a chat engine from the index
chat_engine = index.as_chat_engine(chat_mode="condense_question", llm=llm)

print("🔹 SolaraTech Internal Chatbot 🔹")
print("Ask a question about the employee policy handbook. Type 'exit' to quit.\n")

# Simple loop for chatting
while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        break
    response = chat_engine.chat(query)
    print(f"\n🧠 Bot: {response.response}\n")
