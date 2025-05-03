
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()


# 1. Belgeyi oku ve parçala
loader = TextLoader("average_formula.md")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
splits = splitter.split_documents(docs)

# 2. Vektör veri tabanı
vectorstore = Chroma.from_documents(
    splits,
    embedding=OpenAIEmbeddings(),
    persist_directory="chroma_db"
)

retriever = vectorstore.as_retriever()

from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableMap
from langchain_core.messages import HumanMessage

# 3. LLM zinciri
llm = ChatOpenAI(model="gpt-3.5-turbo")

prompt = PromptTemplate.from_template(
    "Aşağıdaki bağlama göre çalıştırılabilir Python kodu üret. "
    "Kullanıcının belirttiği sütun adlarını doğrudan kullan. "
    "Sonuç 'result' değişkeninde saklanmalı.\n\n"
    "Bağlam:\n{context}\n\nSoru:\n{question}"

)



# retriever zinciri: str input alır, context üretir
retrieval_chain = RunnableMap({
    "context": retriever,
    "question": RunnablePassthrough()
}) | prompt | llm | StrOutputParser()

# Kullanıcıdan gelen komut
command = "A, B ve C sütunlarının özel ortalamasını hesaplayan python kodunu üret"
result = retrieval_chain.invoke(command)

# Sonucu yazdır
print("💡 LLM Cevabı:\n")
print(result)

