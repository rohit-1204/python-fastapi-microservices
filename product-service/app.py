from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
app=FastAPI(title="product-service")
@app.get("/")
def root():
    return {"service":"product-service","status":"running"}
@app.get("/products")
def get_items():
    return JSONResponse(content=json.loads('[{"id":101,"name":"Laptop","price":65000}]'))
