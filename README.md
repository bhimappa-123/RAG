# 📄 RAG-Based PDF Question Answering System

A Retrieval-Augmented Generation (RAG) application that enables users to interact with PDF documents using natural language. The application retrieves the most relevant content from the uploaded document and generates accurate, context-aware responses using Large Language Models (LLMs).

---

## 🚀 Features

- 📄 Upload and process PDF documents
- 🔍 Semantic search using vector embeddings
- 🤖 AI-powered question answering
- 📚 Displays retrieved document chunks
- ⚡ Fast similarity search with FAISS
- 🌐 User-friendly Streamlit interface

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Framework | Streamlit |
| LLM Framework | LangChain |
| Vector Database | FAISS |
| Embedding Model | Hugging Face Embeddings |
| Document Loader | PyPDFLoader |
| Text Processing | RecursiveCharacterTextSplitter |
| Environment Variables | python-dotenv |

---

## 📂 Project Structure

```
RagParacetamolProject/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
├── .env                   # API keys (ignored by Git)
├── .gitignore             # Git ignore rules
├── temp.pdf               # Sample PDF document
├── README.md              # Project documentation
└── myenv/                 # Virtual environment (ignored)
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/bhimappa-123/RAG.git
cd RAG
```

### 2️⃣ Create a Virtual Environment

**Windows**

```bash
python -m venv myenv
myenv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root and add your Hugging Face API token:

```env
HF_TOKEN=your_huggingface_api_token
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

After launching, open the local URL provided by Streamlit in your browser.

---

## 🔄 Workflow

1. Upload a PDF document.
2. Extract text from the document.
3. Split text into manageable chunks.
4. Generate embeddings using Hugging Face.
5. Store embeddings in a FAISS vector database.
6. Retrieve the most relevant chunks based on the user's query.
7. Generate an AI-powered answer using the retrieved context.

---

## 📸 Application Preview

> Add screenshots or a GIF of your application here.

Example:

```
assets/
├── home.png
├── upload.png
└── result.png
```

---

## 📦 Dependencies

- Streamlit
- LangChain
- FAISS
- Hugging Face Transformers
- Sentence Transformers
- PyPDF
- python-dotenv

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🎯 Future Enhancements

- Support for multiple PDF uploads
- Chat history
- Source citation with page numbers
- Conversation memory
- Deploy on Streamlit Community Cloud
- Support for OpenAI, Gemini, and Llama models
- Export chat responses

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Bhimappa Kattennavar**

- 🎓 Electronics & Communication Engineering Graduate
- 💡 Interested in AI, Machine Learning, Data Science, and Full-Stack Development

**GitHub:** https://github.com/bhimappa-123

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub.
