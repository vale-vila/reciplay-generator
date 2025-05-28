# 🎵 Recipe Playlist Generator

A FastAPI application that generates personalized music playlists based on recipes using Claude AI and Spotify integration. Perfect for creating the right cooking atmosphere!

## ✨ Features

- **AI-Powered Playlist Generation**: Uses Claude AI to suggest songs that match your recipe's cuisine, cooking time, and mood
- **Spotify Integration**: Search for songs and create playlists directly in Spotify
- **FastAPI Backend**: Modern, fast web API with automatic documentation
- **Flexible Recipe Input**: Support for various cuisines, cooking times, and difficulty levels
- **CORS Enabled**: Ready for frontend integration

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Anthropic API key (Claude AI)
- Spotify Developer Account and API credentials

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/vale-vila/reciplay-generator.git
   cd reciplay-generator
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   # Claude AI
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   
   # Spotify API
   SPOTIFY_CLIENT_ID=your_spotify_client_id
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
   SPOTIFY_REDIRECT_URI=http://localhost:8000/callback
   ```

### Getting API Keys

#### Anthropic API Key
1. Visit [Anthropic Console](https://console.anthropic.com/)
2. Create an account or sign in
3. Navigate to API Keys section
4. Generate a new API key

#### Spotify API Credentials
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new app
3. Note down your Client ID and Client Secret
4. Add `http://localhost:8000/callback` to your app's redirect URIs

## 🏃‍♂️ Running the Application

### Start the FastAPI server
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### Interactive API Documentation
Visit `http://localhost:8000/docs` for Swagger UI documentation

## 🧪 Testing

### Test Claude AI Connection
```bash
python test_claude.py
```

### Test Full Playlist Creation
```bash
python test_playlist_creation.py
```

## 📚 API Usage

### Generate Playlist

**POST** `/generate-playlist`

```json
{
  "recipe": {
    "name": "Classic Spaghetti Carbonara",
    "cuisine": "Italian",
    "cooking_time": 30,
    "difficulty": "Medium"
  }
}
```

**Response**:
```json
{
  "playlist_name": "Cooking Classic Spaghetti Carbonara - Italian Vibes",
  "songs": [
    "That's Amore - Dean Martin",
    "Volare - Domenico Modugno",
    "Quando Quando Quando - Tony Renis",
    "La Vita È Bella - Nicola Piovani",
    "Mambo Italiano - Rosemary Clooney"
  ],
  "message": "Playlist generated successfully"
}
```

### Test Claude Connection

**GET** `/test-claude`

**Response**:
```json
{
  "status": "success",
  "message": "Claude API connection successful"
}
```

## 🏗️ Project Structure

```
reciplay-generator/
├── main.py                     # FastAPI application entry point
├── claude_service.py          # Claude AI integration
├── spotify_service.py         # Spotify API integration
├── models.py                  # Pydantic data models
├── requirements.txt           # Python dependencies
├── test_claude.py            # Test Claude AI functionality
├── test_playlist_creation.py # Test full playlist creation
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `ANTHROPIC_API_KEY` | Your Claude AI API key | Yes |
| `SPOTIFY_CLIENT_ID` | Spotify app client ID | Yes |
| `SPOTIFY_CLIENT_SECRET` | Spotify app client secret | Yes |
| `SPOTIFY_REDIRECT_URI` | OAuth redirect URI | Yes |

### Recipe Model

```python
class Recipe(BaseModel):
    name: str          # Recipe name
    cuisine: str       # Cuisine type (e.g., "Italian", "Mexican")
    cooking_time: int  # Cooking time in minutes
    difficulty: str    # "Easy", "Medium", or "Hard"
```

## 🎨 Customization

### Modify Claude Prompts
Edit the prompt in `claude_service.py` to customize how playlists are generated:

```python
prompt = f"""Given this recipe:
Name: {recipe.name}
Cuisine: {recipe.cuisine}
...

Generate a list of 5 songs that would be perfect..."""
```

### Adjust Playlist Size
Change the number of songs requested from Claude or modify the search limits in `spotify_service.py`.

## 🐛 Troubleshooting

### Common Issues

1. **"ANTHROPIC_API_KEY not set"**
   - Ensure your `.env` file contains the correct API key
   - Check that the `.env` file is in the root directory

2. **Spotify authentication fails**
   - Verify your Spotify app settings
   - Ensure redirect URI matches exactly
   - Check client ID and secret are correct

3. **No songs found**
   - Claude AI might suggest obscure songs
   - Try different recipe types or cuisines
   - Check Spotify API rate limits

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎯 Future Enhancements

- [ ] Frontend web interface
- [ ] More sophisticated playlist generation algorithms
- [ ] Support for multiple streaming platforms
- [ ] Playlist sharing functionality
- [ ] Recipe ingredient-based song suggestions
- [ ] User preference learning
- [ ] Playlist mood analysis

## 🙏 Acknowledgments

- [Anthropic](https://www.anthropic.com/) for Claude AI
- [Spotify](https://developer.spotify.com/) for the Web API
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework

---

**Happy Cooking & Listening! 🍳🎵**