import os
from dotenv import load_dotenv
from anthropic import Anthropic
from models import Recipe

def main():
    # Load environment variables
    load_dotenv()
    
    try:
        # Initialize Claude client
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable is not set")
        
        client = Anthropic(api_key=api_key)
        model = "claude-3-5-sonnet-20241022"
        
        # Test connection
        print("Testing Claude API connection...")
        response = client.messages.create(
            model=model,
            max_tokens=10,
            messages=[{
                "role": "user",
                "content": "Test connection"
            }]
        )
        print("✅ Connection successful!")
        
        # Create a test recipe for pasta
        test_recipe = Recipe(
            name="Classic Spaghetti",
            cuisine="Italian",
            cooking_time=30,
            difficulty="Easy"
        )
        
        # Generate playlist
        print("\nGenerating playlist for cooking pasta...")
        prompt = f"""Given this recipe:
        Name: {test_recipe.name}
        Cuisine: {test_recipe.cuisine}
        Cooking Time: {test_recipe.cooking_time} minutes
        Difficulty: {test_recipe.difficulty}

        Generate a list of 5 songs that would be perfect to listen to while cooking this recipe.
        Consider the cuisine type, cooking time, and overall mood.
        Return only the song names and artists, one per line."""

        response = client.messages.create(
            model=model,
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        # Split the response into individual songs
        songs = [song.strip() for song in response.content[0].text.split('\n') if song.strip()]
        
        # Print results
        print("\n🎵 Suggested Playlist:")
        print("-" * 40)
        for i, song in enumerate(songs, 1):
            print(f"{i}. {song}")
        print("-" * 40)
        
    except ValueError as e:
        print(f"❌ Configuration Error: {str(e)}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()