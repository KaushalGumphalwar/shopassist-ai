
from sentence_transformers import (SentenceTransformer)

from backend.config import (EMBEDDING_MODEL_NAME)


# Load embedding model once:
model = SentenceTransformer(EMBEDDING_MODEL_NAME)


def generate_embedding(text):
    """
    Generate embedding for a single text.

    Parameters
    ----------
    text : str

    Returns
    -------
    list

    Example:
    --------
    Input:
        "Refunds are processed within 5 days"

    Output:
        [0.12, -0.45, 0.67, ...]
    """

    embedding = model.encode(text)

    return embedding.tolist()


def generate_embeddings(chunks):
    """
    Generate embeddings for all chunks.

    Parameters
    ----------
    chunks : list

    Example:
    --------
    [
        {
            "chunk_id": "faq.txt_0",
            "document_name": "faq.txt",
            "chunk_text": "Frequently Asked Questions..."
        }
    ]

    Returns
    -------
    list

    Example:
    --------
    [
        {
            "chunk_id": "faq.txt_0",
            "document_name": "faq.txt",
            "chunk_text": "Frequently Asked Questions...",
            "embedding": [...]
        }
    ]
    """

    for chunk in chunks:

        chunk["embedding"] = generate_embedding(chunk["chunk_text"])

    return chunks