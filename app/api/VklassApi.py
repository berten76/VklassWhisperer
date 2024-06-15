#from fastapi import FastAPI
from app.services.QueryProcessor import QueryProcessor
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi import FastAPI


class VklassApi:
    def __init__(self, queryProcessor: QueryProcessor):
        print("init")


    def getAnswereFromVklass(self):
        print("getAnswereFromVklass")
        # Here you can process the sentence as needed
        return {"please enter a query"}


    # async def getAnswereFromVklass(sentence: str):
    #     # Here you can process the sentence as needed
    #     return {"processed_sentence": sentence}