from fastapi import FastAPI
from controllers import user

app = FastAPI()
app.include_router(user)
