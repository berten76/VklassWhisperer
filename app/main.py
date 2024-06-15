from app.services.DatabaseCreator import DatabaseCreator
from fastapi import FastAPI
from app.api import vklass_api
from multiprocessing import Process

app = FastAPI()

app.include_router(vklass_api.router)


@app.on_event("startup")
async def startup_event():


    # # Create and start the process
    # p = Process(target=DatabaseCreator(data_path="app/data/vklass", chroma_path="chroma").generate_data_store)
    # p.start()

    # # Wait for the process to finish
    # p.join()
    document_processor = DatabaseCreator(data_path="app/data/vklass", chroma_path="chroma")
    document_processor.generate_data_store()