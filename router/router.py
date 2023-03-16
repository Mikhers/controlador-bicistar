from fastapi import APIRouter

user = APIRouter()


@user.get("/")
def root():
    return {"mensage": "Hi, desde router"}

@user.post("/biciestar/empleados")
def empleados(data_user):
    return {"empleados":"oieodondnf"}
