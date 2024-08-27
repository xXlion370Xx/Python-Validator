from utils import database
from fastapi import FastAPI
from models import cimcnd_model

app = FastAPI()

def get__all_origin():
    data = []
    for r in cimcnd_model.Cimcnd().get_all_records():
        data.append(r)

    return data

@app.get('/get/origin')
async def root():
    
    return get__all_origin()

