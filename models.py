from pydantic import BaseModel, Field
from typing import List, Optional

class Recipe(BaseModel):
    name: str = Field(..., description="Name of the recipe")
    cuisine: str = Field(..., description="Type of cuisine")
    cooking_time: int = Field(..., description="Cooking time in minutes")
    difficulty: str = Field(..., description="Difficulty level (Easy, Medium, Hard)")

class PlaylistRequest(BaseModel):
    recipe: Recipe

class PlaylistResponse(BaseModel):
    playlist_name: str
    songs: List[str]
    message: str

class ErrorResponse(BaseModel):
    error: str
    details: Optional[str] = None