from fastapi import FastAPI
from routes import router

app = FastAPI(
    title= "SMART NOTES"
)


app.include_router(router)