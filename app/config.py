import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Application settings loaded from environment variables."""

    GEMINI_API_Key = os.getenv("GEMINI_API_KEY")
    QDRANT_URL = os.getenv("QDRANT_URL")
    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    QDRANT_COLLECTION = "enterprise_rag"

    GROQ_API_Key = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = "gpt-4o"
    GROQ_FALLBACK_API_Key = os.getenv("GROQ_FALLBACK_API_KEY")


settings = Settings()
