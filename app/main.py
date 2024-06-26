from app.api.VklassApi2 import VklassApi2
from app.services.DatabaseCreator import DatabaseCreator
from app.services.QueryProcessor import QueryProcessor

from app.api import VklassApi
from multiprocessing import Process
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from fastapi import FastAPI

CHROMA_PATH = "chroma"

app = FastAPI()


embedding_function = OpenAIEmbeddings()
chroma_instance = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

db_creator =  DatabaseCreator(data_path="app/data/vklass", chroma_instance=chroma_instance)
db_creator.generate_data_store()

queryProcessor = QueryProcessor(chroma_instance=chroma_instance)
vklassApi = VklassApi2(queryProcessor=queryProcessor)
app.include_router(vklassApi.router)
#app.include_router(vklass_api.router)


# @app.on_event("startup")
# async def startup_event():
#     document_processor = DatabaseCreator(data_path="app/data/vklass", chroma_path="chroma")
#     document_processor.generate_data_store()