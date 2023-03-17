from fastapi import APIRouter
from schema.schemaTablas import Sede
from config.db import conn
from model.users import sede

user = APIRouter()


@user.get("/")
def root():
    return {"mensage": "Hi, desde router"}

@user.post("/insert-sede")
def insertSede(data: Sede):
    new_data = data.dict()
    print(new_data)
    print(data)
    conn.execute(sede.insert().values(new_data))
    conn.commit()
    return "Success"

