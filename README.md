<h1 align="center">Real-time AI ChatBot and voice-enabled AI VoiceBot</h1>
<br>
<p align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
  <img src="https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain">
  <img src="https://img.shields.io/badge/groq-FF6600?style=for-the-badge&logo=groq&logoColor=white" alt="Groq">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI">
  <img src="https://img.shields.io/badge/deepgram-13EF93?style=for-the-badge&logo=deepgram&logoColor=black" alt="Deepgram">
</p>
<br>

🔊 Real-Time Voice AI Assistant using Groq LLaMA3 + Deepgram + LangChain .

This project is a real-time voice-based conversational AI assistant that integrates:

   🧠 Groq’s LLaMA3 (via LangChain) for ultra-fast, high-quality conversational intelligence
   
   🎙️ Deepgram STT (Speech-to-Text) for real-time transcription from microphone input
   
   🗣️ Deepgram TTS (Text-to-Speech) for fast and natural voice responses using ffplay
   
Core components such as LLM (Large Language Model), STT (Speech to Text Model), TTS (Text to Speech Model), and the overall Chatbot architecture have also been documented to support comprehensive understanding and customization.

## Features

- Real-time voice recognition using Deepgram
- AI-powered responses via Groq LLM
- Easy setup with virtual environment
- Cross-platform compatibility

## Installation

### Step 1: Clone the Repository

**Option A: Using VS Code Terminal**
1. Open Visual Studio Code
2. Open a new terminal (Terminal → New Terminal or `Ctrl+Shift+`` )
3. Navigate to your desired directory:
   ```bash
   cd path/to/your/desired/folder
   ```
4. Clone the repository:
   ```bash
   git clone https://github.com/Sharan-Kumar-R/Voice-Chat-Bot.git
   ```
5. Open the project folder:
   ```bash
   cd voice-chat-agent
   ```
6. Open the project in VS Code:
   ```bash
   code .
   ```

**Option B: Using VS Code Git Integration**
1. Open Visual Studio Code
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
3. Type "Git: Clone" and select it
4. Paste the repository URL: `https://github.com/Sharan-Kumar-R/Voice-Chat-Bot.git`
5. Choose a folder location and click "Select Repository Location"
6. Click "Open" when prompted

### Step 2: Install FFmpeg

1. Visit [FFmpeg Download Page](https://www.ffmpeg.org/download.html)
2. Download the appropriate version for your operating system
3. Follow the installation instructions for your platform
4. Verify the installation by opening a terminal/command prompt and typing:
   ```bash
   ffmpeg --version
   ```
   If FFmpeg is properly installed, you should see version information displayed.

### Step 3: Create Virtual Environment

Open a terminal in Visual Studio Code and run:

```bash
python -m venv myenv
```

### Step 4: Activate Virtual Environment

**For Windows:**
```bash
myenv\Scripts\activate
```

**For macOS/Linux:**
```bash
source myenv/bin/activate
```

After activation, you should see something like this in your terminal:
```
(myenv) PS C:\Users\username\path\to\project>
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```
## API Setup

### 1. Groq API Key

1. Visit [Groq Console](https://groq.com/)
2. Create an account or sign in
3. Generate a new API key
4. Copy the API key for later use

### 2. Deepgram API Key

1. Visit [Deepgram Console](https://console.deepgram.com/)
2. Create an account or sign in
3. Generate a new API key
4. Copy the API key for later use

### 3. Environment Configuration

Create a `.env` file in the project root directory and add your API keys (replace if already exists):

```env
GROQ_API_KEY=your_groq_api_key_here
DEEPGRAM_API_KEY=your_deepgram_api_key_here
```

**Important:** Replace `your_groq_api_key_here` and `your_deepgram_api_key_here` with your actual API keys.

## Usage

### Running the Voice Bot

1. Make sure your virtual environment is activated:
   ```bash
   myenv\Scripts\activate
   ```

2. Run the main voice bot application:
   ```bash
   python Voice_Bot.py
   ```
3. **Start talking!** The bot will:
   - Listen to your voice input
   - Process it through Groq LLaMA3
   - Respond with natural speech

### Customizing the Bot

To customize the bot's behavior, such as naming the model and defining its function, edit the `Bot_prompt.txt` file.

### Running Other Scripts

To run any other Python file in the project:
```bash
python <filename>.py
```

## Deactivating the Environment

When you're done working with the project, deactivate the virtual environment:

```bash
deactivate
```

## Troubleshooting

- Ensure your API keys are correctly set in the `.env` file
- Make sure your virtual environment is activated before running any scripts
- Check that all dependencies are installed with `pip list`
- Verify your internet connection for API services
- **FFmpeg Issues**: If you encounter audio-related errors, verify FFmpeg installation with `ffmpeg --version`

## Project Structure

```
voice-bot-project/
├── .env                     # Environment variables (API keys)
├── Chat_Bot.py              # Chat bot implementation
├── llm.py                   # Language model integration
├── Voice_Bot.py             # Main voice bot application
├── README.md                # This documentation
├── requirements.txt         # Python dependencies
├── speech_to_text.py        # Speech-to-text streaming functionality
├── Bot_prompt.txt           # System prompt configuration
├── text_to_speech.py        # Text-to-speech functionality
└── myenv/                   # Virtual environment folder (created during setup)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

In case of any queries, please leave a message or contact me via the email provided in my profile.
<div align="center">

# Social Media Scraper - Custom MCP Server

</div>

A comprehensive Model Context Protocol (MCP) server that provides social media scraping capabilities for LinkedIn, Facebook, Instagram, and Google search functionality.

## What is MCP?

**[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction)** is an open standard that enables AI assistants to securely connect with external data sources and tools. MCP servers act as bridges between AI models and various services, allowing for enhanced capabilities like real-time data access, API integrations, and custom tool execution.

## Features

This server exposes the following tools for an AI assistant to use:

- **LinkedIn Profile Scraping**: Extract personal and company profile data
- **Facebook Profile Scraping**: Fetch public profile information
- **Instagram Profile Scraping**: Get profile data and basic information
- **Google Search**: Perform web searches using Google Serper API

## Installation

### Step 1: Adding MCP to your Python project

We recommend using [uv](https://docs.astral.sh/uv/) to manage your Python projects.

If you haven't created a uv-managed project yet, create one:

```bash
uv init custom-mcp-server
cd custom-mcp-server
```

### Step 2: Install MCP Dependencies

Then add MCP to your project dependencies:

```bash
uv add "mcp[cli]"
```

This will auto-generate files and folders similar to the project structure mentioned below, also create a .env file to securely store the API keys.

### Step 3: Add Project Code

In the files generated look for main.py and copy paste the code given in main.py (repo).

### Step 4: Install Additional Dependencies

```bash
uv add httpx python-dotenv fastmcp
```

## Environment Configuration

### Step 1: API Keys Setup

1. **RapidAPI Key**: 
   - Sign up at [RapidAPI](https://rapidapi.com/)
   - Subscribe to the following APIs (Most Important):
     - Fresh LinkedIn Profile Data
     - Facebook Scraper3
     - Instagram Scraper Stable API

2. **Google Serper API Key**:
   - Sign up at [Serper.dev](https://serper.dev/)
   - Get your API key from the dashboard

### Step 2: Environment Variables

Create a `.env` file in your project root with the following variables:

```env
RAPIDAPI_KEY=your_rapidapi_key_here
SERPER_API_KEY=your_serper_api_key_here
```

## Usage

### Running with Claude Desktop

#### Step 1: Install the Server

You can install this server in [Claude Desktop](https://claude.ai/download) and interact with it right away by running:

```bash
mcp install main.py
```

#### Step 2: Verify Installation

Later, go to Claude AI (desktop version) and you will see changes in the platform similar to the [screenshot shown](https://github.com/Sharan-Kumar-R/Custom-MCP-Server/blob/main/Claude_View.png).

#### Step 3: Start Using the Tools

Paste the URLs of required platform and ask the AI to provide information of the mentioned URLs.

### Example Usage

```
Please scrape this LinkedIn profile: https://linkedin.com/in/example-profile
```

```
Get company information for: https://linkedin.com/company/example-company
```

## Troubleshooting

If the MCP tools don't appear in Claude Desktop:

#### Step 1: End Claude Processes

- **Windows**: Open Task Manager (Ctrl+Shift+Esc)
- **Mac**: Open Activity Monitor
- End all Claude-related processes

#### Step 2: Reinstall the Server

```bash
mcp install main.py
```

#### Step 3: Restart Claude Desktop

Paste the URLs of required platform and ask the AI to provide information of the mentioned URLs.

### Testing with MCP Inspector

Alternatively, you can test it with the MCP Inspector:

```bash
mcp dev main.py
```

## Project Structure

```
custom-mcp-server/
├── __pycache__/          # Python bytecode cache (auto-generated)
├── .venv/                # Virtual environment directory
├── .env                  # Environment variables (API keys)
├── .python-version       # Python version specification
├── main.py               # Main MCP server implementation
├── pyproject.toml        # Project configuration and dependencies
├── README.md             # Project documentation
└── uv.lock               # UV lock file for reproducible builds
```

## Response Format

All tools return JSON-formatted strings containing the scraped data. Example response structure:

```json
{
  "success": true,
  "data": {
    "profile": {
      "name": "John Doe",
      "title": "Software Engineer",
      "location": "San Francisco, CA",
      "bio": "Passionate about technology..."
    }
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
```

But using these tools via Claude makes it readable.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

In case of any queries, please leave a message or contact me via the email provided in my profile.

---

<p align="center">
⭐ <strong>Star this repository if you found it helpful!</strong>
</p>
<p align="center">
⭐ <strong>Star this repository if you found it helpful!</strong>
</p>
