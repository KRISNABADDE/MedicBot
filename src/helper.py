from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import CTransformers


def download_hugging_face_embeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings


def QuestionAnswer(docsearch):
    qa=RetrievalQA.from_chain_type(
            llm=llm, 
            chain_type="stuff", 
            retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
            return_source_documents=True, 
            chain_type_kwargs=chain_type_kwargs)
    return qa


def LoadLLM(path,model_type="llama"):
    llm=CTransformers(model=path,
                      model_type="llama",
                      config={'max_new_tokens':512,
                              'temperature':0.8})
    return llm



