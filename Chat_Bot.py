from dotenv import load_dotenv
import time
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain

load_dotenv()

class LanguageModelProcessor:
    def __init__(self):
        groq_api_key = os.getenv("GROQ_API_KEY")
        
        if groq_api_key:
            self.llm = ChatGroq(temperature=0, model_name="llama3-8b-8192", groq_api_key=groq_api_key)
        else:
            raise ValueError("GROQ_API_KEY not found in environment variables. Please set one.")

        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        # Load Bot prompt
        try:
            with open('Bot_prompt.txt', 'r') as file:
                Bot_prompt = file.read().strip()
        except FileNotFoundError:
            raise FileNotFoundError("Bot prompt file 'Bot_prompt.txt' not found. Please ensure it exists in the current directory.")

        self.prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(Bot_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{text}")
        ])

        self.conversation = LLMChain(
            llm=self.llm,
            prompt=self.prompt,
            memory=self.memory
        )

    def process(self, text):
        response = self.conversation.invoke({"text": text})
        return response['text']


class ConversationManager:
    def __init__(self):
        self.llm_processor = LanguageModelProcessor()
        print()
        print("Chatbot initialized. Type 'goodbye' to end.")
        print()

    def main(self):
        while True:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit", "goodbye"]:
                print("Bot: Goodbye!")
                break

            llm_response = self.llm_processor.process(user_input)
            print(f"🤖  : {llm_response}")
            print()

if __name__ == "__main__":
    manager = ConversationManager()
    manager.main()
