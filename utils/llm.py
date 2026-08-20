import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


# Load variables from .env
load_dotenv()


# Get Groq settings
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")


if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing. "
        "Please add it to your .env file."
    )


if not GROQ_MODEL:
    raise ValueError(
        "GROQ_MODEL is missing. "
        "Please add it to your .env file."
    )


# Create Groq LLM
llm = ChatOpenAI(
    model=GROQ_MODEL,
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
    temperature=0.2,
)