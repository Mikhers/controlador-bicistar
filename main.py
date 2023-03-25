from fastapi import FastAPI
from router.get import gets
from router.put import puts
from router.delete import deletes
from router.post import posts

# from fastapi.middleware.cors import CORSMiddleware

# origins = ["*"]
# methods = ["*"]
# allow_headers = ["*"]

app = FastAPI()
app.title = "BICISTAR-API"

app.include_router(gets)
app.include_router(posts)
app.include_router(puts)
app.include_router(deletes)

# app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=methods, allow_headers=allow_headers, allow_credentials=True, expose_headers=["*"])