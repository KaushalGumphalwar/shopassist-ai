import os

from dotenv import load_dotenv

# Load Environment Variables:
load_dotenv()

# Project Paths:
# --------------

# Folder containing client documents:
DATA_FOLDER = "client_docs"

# ChromaDB persistent storage location:
VECTOR_DB_PATH = "vectorstores"

# Folder for storing uploaded files (future FastAPI upload support):
UPLOAD_FOLDER = "uploads"


# ChromaDB Configuration:
# -----------------------
COLLECTION_NAME = "shopassist_collection"


# Chunking Configuration:
# -----------------------
CHUNK_SIZE = 250
CHUNK_OVERLAP = 50


# Embedding Model:
# ----------------
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"


# Retrieval Configuration:
# ------------------------
TOP_K = 3


# Gemini Configuration:
# ---------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-2.0-flash"


# Document Update Tracking:
# -------------------------
HASH_FILE = "document_hashes.json"


# Logging Configuration:
# ----------------------
LOG_LEVEL = "INFO"