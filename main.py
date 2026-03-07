import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from notes_routes import router as notes
from user_routes import router as user

from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title= "SMART NOTES"
)


app.include_router(notes, tags=["Notes"], prefix="/notes")
app.include_router(user, tags=["Users"], prefix="/users")


frontend = "Frontend/"

app.mount("/", StaticFiles(directory=frontend, html=True), name="frontend")


@app.get("/", include_in_schema=False)
async def redirect_to_Frontend():
    return RedirectResponse(url="/Frontend/index.html", status_code=302) 