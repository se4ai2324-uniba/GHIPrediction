"""module for APIs"""
from fastapi import FastAPI
from app.schema import Xgbooster

app=FastAPI()

@app.get("/")
def root():
    return{
        "message":"hi"
        }

