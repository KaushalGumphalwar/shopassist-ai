import chromadb

from backend.config import (VECTOR_DB_PATH, COLLECTION_NAME)


# Create ChromaDB Client:
client = chromadb.PersistentClient(path=VECTOR_DB_PATH)

# Get/Create Collection:
collection = client.get_or_create_collection(name=COLLECTION_NAME)


def get_collection():
    """
    Return ChromaDB collection.

    Returns
    -------
    Collection
    """

    return collection


def store_chunks(chunks):
    """
    Store chunks and embeddings into ChromaDB.

    Parameters
    ----------
    chunks : list

    Example:
    --------
    [
        {
            "chunk_id": "faq.txt_0",

            "document_name": "faq.txt",

            "chunk_text":
            "How can I track my order?",

            "embedding":
            [0.12, -0.55, 0.87]
        }
    ]
    """

    for chunk in chunks:

        collection.add(
                        ids = [chunk["chunk_id"]],
                        documents = [chunk["chunk_text"]],
                        embeddings = [chunk["embedding"]],
                        metadatas = [{"document_name": chunk["document_name"]}]
                     )

def delete_document_vectors(document_name):
    """
    Delete old embeddings.
    """

    collection.delete(where={"document_name": document_name})