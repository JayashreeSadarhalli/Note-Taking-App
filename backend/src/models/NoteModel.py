from typing import List

from pydantic import BaseModel
from src.models.ObjectId import ObjectId


class NoteInputModel(BaseModel):
    message: str
    is_deleted: bool = False
    created_at: int
    updated_at: int


class NoteList(BaseModel):
    notes: List[NoteInputModel]


class BasicSucessModel(BaseModel):
    response: str = "success"
