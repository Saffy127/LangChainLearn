from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

def query_pdf(pdf_path, query):
    # Load the PDF
    loader = PyPDFLoader(pdf_path)

    # Split the PDF into pages
    pages = loader.load_and_split()

    # Create a ChatOpenAI object
    chat = ChatOpenAI()

    # Create an OpenAIEmbeddings object
    embeddings = OpenAIEmbeddings()

    # Create a Chroma object from the pages and embeddings
    db = Chroma.from_documents(pages, embeddings)

    # Create a retriever from the Chroma object
    retriever = db.as_retriever()

    # Create a RetrievalQA object from the chat model and retriever
    qa = RetrievalQA.from_chain_type(llm=chat, retriever=retriever)

    # Run the query and return the result
    return qa.run(query)
