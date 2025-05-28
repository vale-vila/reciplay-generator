from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Recipe, PlaylistRequest, PlaylistResponse, ErrorResponse
from claude_service import ClaudeService
from spotify_service import SpotifyService
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Recipe Playlist Generator",
    description="Generate playlists based on recipes using Claude AI",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
claude_service = ClaudeService()
spotify_service = SpotifyService()

@app.post("/generate-playlist", response_model=PlaylistResponse, responses={400: {"model": ErrorResponse}, 500: {"model": ErrorResponse}})
async def generate_playlist(request: PlaylistRequest):
    try:
        # Generate playlist using Claude
        songs = await claude_service.generate_playlist(request.recipe)
        
        # Create playlist name based on recipe
        playlist_name = f"Cooking {request.recipe.name} - {request.recipe.cuisine} Vibes"
        
        return PlaylistResponse(
            playlist_name=playlist_name,
            songs=songs,
            message="Playlist generated successfully"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"error": "Failed to generate playlist", "details": str(e)}
        )

@app.get("/test-claude", response_model=dict, responses={500: {"model": ErrorResponse}})
async def test_claude():
    try:
        is_connected = await claude_service.test_connection()
        return {"status": "success", "message": "Claude API connection successful"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"error": "Failed to connect to Claude API", "details": str(e)}
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)