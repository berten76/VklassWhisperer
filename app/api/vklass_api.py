#from fastapi import FastAPI
from app.services.QueryProcessor import QueryProcessor
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str


router = APIRouter()
query_processor = QueryProcessor()

# @router.post("/query")
# async def handle_query(request: QueryRequest):
#     try:
#         response = query_processor.process_query(request.query)
#         return {"response": response}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
# @app.get("/")
# async def read_item():
#     return {"message": "welcome"}

@router.get("/")
async def getAnswereFromVklass():
    print("getAnswereFromVklass")
    # Here you can process the sentence as needed
    return {"please enter a query"}

@router.get("/process_sentence/")
async def getAnswereFromVklass(sentence: str):
    # Here you can process the sentence as needed
    return {"processed_sentence": sentence}