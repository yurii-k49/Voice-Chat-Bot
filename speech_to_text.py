import asyncio
from dotenv import load_dotenv
from deepgram import (
    DeepgramClient,
    DeepgramClientOptions,
    LiveTranscriptionEvents,
    LiveOptions,
    Microphone,
)

# Load environment variables (e.g., Deepgram API key from .env file)
load_dotenv()

class TranscriptManager:
    """
    Collects and manages transcript fragments during streaming.
    """
    def __init__(self):
        self.fragments = []

    def add_fragment(self, text: str):
        self.fragments.append(text)

    def get_combined_transcript(self) -> str:
        return ' '.join(self.fragments).strip()

    def reset(self):
        self.fragments.clear()

async def transcribe_from_microphone():
    """
    Streams audio from the microphone to Deepgram and prints transcripts live.
    """
    try:
        client_config = DeepgramClientOptions(options={"keepalive": "true"})
        dg_client = DeepgramClient("", client_config)
        dg_stream = dg_client.listen.asynclive.v("1")

        transcript_manager = TranscriptManager()
        terminate_event = asyncio.Event()

        async def handle_transcript(_, result, **kwargs):
            if not result.channel.alternatives:
                return
            text = result.channel.alternatives[0].transcript.strip()

            if not text:
                return  # Skip empty transcripts

            if not result.speech_final:
                transcript_manager.add_fragment(text)
            else:
                transcript_manager.add_fragment(text)
                full_text = transcript_manager.get_combined_transcript()
                if full_text:  # Only print if there's actual speech
                    print(f"Speaker: {full_text}")

                    if "goodbye" in full_text.lower():
                        terminate_event.set()
                transcript_manager.reset()

        async def handle_error(_, error, **kwargs):
            print(f"[Error] {error}")

        dg_stream.on(LiveTranscriptionEvents.Transcript, handle_transcript)
        dg_stream.on(LiveTranscriptionEvents.Error, handle_error)

        options = LiveOptions(
            model="nova-2",
            punctuate=True,
            language="en-US",
            encoding="linear16",
            channels=1,
            sample_rate=16000,
            endpointing=True
        )

        await dg_stream.start(options)

        mic = Microphone(dg_stream.send)
        mic.start()
        
        print()
        print("Listening.......")
        print("Say 'goodbye' to end the session.")
        print()

        while mic.is_active() and not terminate_event.is_set():
            await asyncio.sleep(0.5)

        mic.finish()
        await dg_stream.finish()
        print("Session ended.")

    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == "__main__":
    asyncio.run(transcribe_from_microphone())
