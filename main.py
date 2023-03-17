from fastapi import FastAPI
from router.router import bicistar

app = FastAPI()


app.include_router(bicistar)