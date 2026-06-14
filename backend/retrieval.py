from backend.embeddings import (generate_embedding)

from backend.vectorstore import (get_collection)

from backend.config import (TOP_K)


def retrieve_chunks(query):
    """
    Retrieve top relevant chunks.

    Parameters
    ----------
    query : str

    Example:
    --------
    "How long does refund take?"

    Returns
    -------
    dict

    ChromaDB query result
    """

    # Step 1:
    # Generate query embedding

    query_embedding = generate_embedding(query)

    # Step 2:
    # Load collection

    collection = get_collection()

    # Step 3:
    # Similarity search

    results = collection.query(
                                query_embeddings=[query_embedding],
                                n_results=TOP_K
                              )
    
    print("\n========== DOCUMENTS ==========")
    print(results["documents"])

    print("\n========== METADATAS ==========")
    print(results["metadatas"])
 
    return results