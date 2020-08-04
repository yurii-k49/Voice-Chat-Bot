import os
import requests
import subprocess
import shutil
import time
from dotenv import load_dotenv

# Load environment variables (ensure your .env contains DEEPGRAM_API_KEY)
load_dotenv()

API_KEY = os.getenv("DEEPGRAM_API_KEY")
MODEL = "aura-asteria-en"  # Replace with your preferred model

def command_available(cmd: str) -> bool:
    """Check if a command-line tool is available in the system PATH."""
    return shutil.which(cmd) is not None

def stream_audio_from_chunks(audio_chunks):
    """Play audio stream chunks using ffplay."""
    if not command_available("ffplay"):
        raise RuntimeError("ffplay not found on system. Please install ffmpeg to proceed.")

    ffplay_process = subprocess.Popen(
        ["ffplay", "-autoexit", "-nodisp", "-"],
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    for chunk in audio_chunks:
        if chunk and ffplay_process.stdin:
            ffplay_process.stdin.write(chunk)
            ffplay_process.stdin.flush()

    if ffplay_process.stdin:
        ffplay_process.stdin.close()

    ffplay_process.wait()

def tts_request_and_play(text: str):
    """Send text to Deepgram's TTS API and play the returned audio stream."""
    url = f"https://api.deepgram.com/v1/speak?model={MODEL}&encoding=linear16&sample_rate=24000"
    headers = {
        "Authorization": f"Token {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {"text": text}

    print("Sending request to Deepgram TTS...")
    start_time = time.time()
    first_byte_time = None

    with requests.post(url, headers=headers, json=payload, stream=True) as response:
        if response.status_code != 200:
            print(f"Error {response.status_code}: {response.text}")
            return

        def audio_generator():
            nonlocal first_byte_time
            for data in response.iter_content(chunk_size=1024):
                if data:
                    if first_byte_time is None:
                        first_byte_time = time.time()
                        ttfb = int((first_byte_time - start_time) * 1000)
                        print(f"Time to First Byte (TTFB): {ttfb} ms")
                    yield data

        stream_audio_from_chunks(audio_generator())

if __name__ == "__main__":
    input_text = input("Enter text to convert to speech: ").strip()
    if input_text:
        tts_request_and_play(input_text)
    else:
        print("No text provided.")
