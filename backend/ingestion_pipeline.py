from backend.document_loader import (load_documents)

from backend.chunking import (create_chunks)

from backend.embeddings import (generate_embeddings)

from backend.vectorstore import (store_chunks)


def run_ingestion():
    """
    Execute complete ingestion workflow.
    """

    print("Loading documents...")

    documents = load_documents()

    print(f"Loaded {len(documents)} documents")

    print("Creating chunks...")

    chunks = create_chunks(documents)

    print(f"Created {len(chunks)} chunks")

    print("Generating embeddings...")

    chunks = generate_embeddings(chunks)

    print("Storing embeddings in ChromaDB...")

    store_chunks(chunks)

    print("Document ingestion completed successfully.")


if __name__ == "__main__":

    run_ingestion()