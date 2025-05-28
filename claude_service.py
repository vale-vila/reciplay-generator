import os
from anthropic import Anthropic
from typing import List
from models import Recipe

class ClaudeService:
    def __init__(self):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable is not set")
        self.client = Anthropic(api_key=api_key)
        self.model = "claude-3-5-sonnet-20241022"

    async def generate_playlist(self, recipe: Recipe) -> List[str]:
        try:
            prompt = f"""Given this recipe:
            Name: {recipe.name}
            Cuisine: {recipe.cuisine}
            Cooking Time: {recipe.cooking_time} minutes
            Difficulty: {recipe.difficulty}

            Generate a list of 5 songs that would be perfect to listen to while cooking this recipe.
            Consider the cuisine type, cooking time, and overall mood.
            Return only the song names and artists, one per line."""

            response = await self.client.messages.create(
                model=self.model,
                max_tokens=1000,
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )
            
            # Split the response into individual songs
            songs = [song.strip() for song in response.content[0].text.split('\n') if song.strip()]
            return songs

        except Exception as e:
            raise Exception(f"Error generating playlist with Claude: {str(e)}")

    async def test_connection(self) -> bool:
        try:
            await self.client.messages.create(
                model=self.model,
                max_tokens=10,
                messages=[{
                    "role": "user",
                    "content": "Test connection"
                }]
            )
            return True
        except Exception as e:
            raise Exception(f"Error testing Claude connection: {str(e)}")