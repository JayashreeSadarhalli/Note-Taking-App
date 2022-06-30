from fastapi import APIRouter, Request
from backend.src.models.NoteModel import BasicSucessModel, NoteInputModel


router = APIRouter(prefix="/notes")


@router.post("", response_model=BasicSucessModel)
async def create_note(request: Request, note: NoteInputModel):
    inserted_event = await request.app.mongodb.notesapp.notes.insert_one(note)
    return BasicSucessModel


@router.get("/o")
async def hi():
    return "hi"
