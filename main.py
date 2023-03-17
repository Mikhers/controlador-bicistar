from fastapi import FastAPI
from router.router import bicistar

app = FastAPI()
app.title = "BICISTAR-API"

app.include_router(bicistar)