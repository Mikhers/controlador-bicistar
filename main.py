from fastapi import FastAPI
from router.get import gets
from router.put import puts
from router.delete import deletes
from router.post import posts

app = FastAPI()
app.title = "BICISTAR-API"

app.include_router(gets)
app.include_router(posts)
app.include_router(puts)
app.include_router(deletes)