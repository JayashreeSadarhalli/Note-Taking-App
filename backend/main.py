import base64
import json
import sys
import time

import uvicorn
from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import PlainTextResponse
from src.models.NoteModel import BasicSucessModel, NoteInputModel

from src.config import settings

app = FastAPI(title="Notes API", version=settings.VERSION)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.on_event("startup")
async def startup_db_client():
    app.mongodb = AsyncIOMotorClient(settings.MONGODB_URL)


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb.close()


@app.post("/notes")
async def create_note(request: Request, note: NoteInputModel):
    inserted_note = await request.app.mongodb.notesapp.notes.insert_one(note.dict())
    return "success"


@app.get("/notes")
async def hi():
    return "hi"


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )
