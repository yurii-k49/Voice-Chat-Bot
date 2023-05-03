import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables (e.g., GROQ_API_KEY)
load_dotenv()

def create_chain(model_name: str, system_message: str, user_placeholder: str):
    """
    Creates a LangChain chain with specified model, system message, and user input placeholder.
    """
    chat = ChatGroq(
        temperature=0,
        model_name=model_name,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("human", user_placeholder)
    ])
    return prompt | chat

def run_batch(prompt_text: str):
    """
    Runs a single-shot (batch) completion.
    """
    chain = create_chain(
        model_name="llama3-70b-8192",
        system_message="You are an AI assistant designed to provide helpful answers.",
        user_placeholder="{input}"
    )
    result = chain.invoke({"input": prompt_text})
    print("\nBatch Response:\n", result.content)

def run_streaming(prompt_text: str):
    """
    Runs streaming completion and prints output as it arrives.
    """
    chain = create_chain(
        model_name="llama3-70b-8192",
        system_message="You are an AI assistant that provides thoughtful, detailed responses.",
        user_placeholder="{input}"
    )
    print("\nStreaming Response:\n")
    for chunk in chain.stream({"input": prompt_text}):
        print(chunk.content, end="", flush=True)

if __name__ == "__main__":
    mode = input("Select mode ('batch' or 'streaming'): ").strip().lower()
    user_input = input("Enter your prompt: ").strip()
    
    if mode == "batch":
        run_batch(user_input)
    elif mode == "streaming":
        run_streaming(user_input)
    else:
        print("Invalid mode selected. Please choose 'batch' or 'streaming'.")
