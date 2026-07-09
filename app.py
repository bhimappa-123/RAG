import streamlit as st
import os
from dotenv import load_dotenv


load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from transformers import pipeline
from langchain.llms import HuggingFacePipeline


st.set_page_config(page_title="RAG PDF QA", layout="centered")
st.title("Document Question Answering System")

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])


if uploaded_file is not None:
    
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully ")

    
    loader = PyPDFLoader("temp.pdf")
    documents = loader.load()

    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    texts = text_splitter.split_documents(documents)
    st.write(f"Total Chunks Created: {len(texts)}")

    
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    
    vectorstore = FAISS.from_documents(texts, embeddings)

    
    query = st.text_input("Ask a question from the document")

    if query:
        with st.spinner("Thinking..."):
            
            retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
            docs = retriever.get_relevant_documents(query)

            
            st.subheader("Retrieved Chunks")
            for i, doc in enumerate(docs):
                st.write(f"**Chunk {i+1}:**")
                st.write(doc.page_content)
                st.write("---")

            
            context = " ".join([doc.page_content for doc in docs])

            
            hf_pipeline = pipeline(
                task="text-generation",
                model="google/flan-t5-base",
                token=HF_TOKEN,
                max_length=512,
                temperature=0.7
            )

            llm = HuggingFacePipeline(pipeline=hf_pipeline)

            prompt = f"""
            You are an AI assistant.Using the context below, generate a clear and simple answer
            in your own words. Do not copy sentences exactly.

            Context:
            {context}

            Question:
            {query}
            """

            
            answer = llm.invoke(prompt)

            
            st.subheader("Final Answer")
            st.write(answer)