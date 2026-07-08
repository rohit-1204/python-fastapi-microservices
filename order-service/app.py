from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
app=FastAPI(title="order-service")
@app.get("/")
def root():
    return {"service":"order-service","status":"running"}
@app.get("/orders")
def get_items():
    return JSONResponse(content=json.loads('[{"id":1001,"user":1,"product":101}]'))
