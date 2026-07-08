from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
app=FastAPI(title="user-service")
@app.get("/")
def root():
    return {"service":"user-service","status":"running"}
@app.get("/users")
def get_items():
    return JSONResponse(content=json.loads('[{"id":1,"name":"Rohit","city":"Pune"}]'))
