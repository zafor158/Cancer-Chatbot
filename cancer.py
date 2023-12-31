##%%writefile app.py

import streamlit as st
import random
import time

from langchain.document_loaders import PyPDFLoader, OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone
from sentence_transformers import SentenceTransformer
from langchain.chains.question_answering import load_qa_chain
import pinecone
import os

loader = PyPDFLoader("Cancer_chat_bot.zip/cancer_data.pdf")

data = loader.load()



text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

docs=text_splitter.split_documents(data)


os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY', '2e51597b-dc66-40e9-b459-7616de83716d')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV', 'gcp-starter')


embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')


# initialize pinecone
pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment=PINECONE_API_ENV  # next to api key in console
)
index_name = "cancerpinecone" # put in the name of your pinecone index here


docsearch=Pinecone.from_texts([t.page_content for t in docs], embeddings, index_name=index_name)


def getResponse(prompt):

  docs=docsearch.similarity_search(prompt)

  length = -9999999;
  ans = ""

  for doc in docs:
    if len(doc.page_content) > length and "\n" not in doc:
      length = len(doc.page_content)
      ans = doc.page_content


  return ans


st.title("Medical chat bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = getResponse(prompt)
        print(prompt)
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
