import os
from datetime import datetime
from dotenv import load_dotenv
from anthropic import Anthropic
from spotify_service import SpotifyService
import re

def parse_claude_songs(response_text: str) -> list[str]:
    """Extract song names and artists from Claude's response."""
    # Split by newlines and filter out empty lines
    lines = [line.strip() for line in response_text.split('\n') if line.strip()]
    
    # Remove any numbering (e.g., "1. ", "2. ", etc.)
    songs = [re.sub(r'^\d+\.\s*', '', line) for line in lines]
    
    return songs

def main():
    # Load environment variables
    load_dotenv()
    
    try:
        print("🎵 Starting Recipe Playlist Generator Test")
        print("-" * 50)
        
        # Step 1: Initialize Claude
        print("\n🤖 Initializing Claude...")
        claude = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        
        # Step 2: Get song suggestions from Claude
        print("\n🎼 Getting song suggestions from Claude...")
        prompt = """Generate a list of 5 romantic Italian songs that would be perfect for cooking a romantic Italian dinner.
        Return only the song names and artists, one per line.
        Example format:
        That's Amore - Dean Martin
        Volare - Dean Martin"""
        
        response = claude.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        # Step 3: Parse Claude's response
        print("\n📝 Parsing Claude's suggestions...")
        suggested_songs = parse_claude_songs(response.content[0].text)
        print("\nSuggested songs:")
        for i, song in enumerate(suggested_songs, 1):
            print(f"{i}. {song}")
        
        # Step 4: Initialize Spotify with user authentication
        print("\n🎧 Initializing Spotify...")
        spotify = SpotifyService(use_user_auth=True)
        
        # Step 5: Get current user
        print("\n👤 Getting Spotify user information...")
        user = spotify.get_current_user()
        if not user:
            raise Exception("Failed to get Spotify user information")
        print(f"Logged in as: {user['display_name']}")
        
        # Step 6: Search for songs on Spotify
        print("\n🔍 Searching for songs on Spotify...")
        found_tracks = spotify.search_songs(suggested_songs)
        
        if not found_tracks:
            raise Exception("No songs were found on Spotify")
        
        # Step 7: Create playlist
        print("\n📋 Creating playlist...")
        playlist_name = f"Recipe Beats Test - {datetime.now().strftime('%Y-%m-%d')}"
        track_ids = [track["id"] for track in found_tracks]
        
        playlist = spotify.create_playlist(
            user_id=user["id"],
            playlist_name=playlist_name,
            track_ids=track_ids
        )
        
        if not playlist:
            raise Exception("Failed to create playlist")
        
        # Step 8: Print results
        print("\n✨ Success!")
        print("-" * 50)
        print(f"🎵 Playlist created: {playlist['name']}")
        print(f"🔗 Playlist URL: {playlist['url']}")
        print(f"📊 Tracks added: {playlist['track_count']}")
        print("\nAdded tracks:")
        for track in found_tracks:
            print(f"• {track['name']} by {track['artist']}")
        print("-" * 50)
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())