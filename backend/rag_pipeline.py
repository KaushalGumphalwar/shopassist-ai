from backend.retrieval import (retrieve_chunks)

from backend.llm_service import (generate_answer)


def ask_question(query):
    """
    Execute complete RAG workflow.

    Parameters
    ----------
    query : str

    Example:
    --------
    "How long does refund take?"

    Returns
    -------
    dict
    """

    # Step 1:
    # Retrieve relevant chunks

    retrieval_results = retrieve_chunks(query)

    print("\n========== DOCUMENTS ==========")
    print(retrieval_results["documents"])

    print("\n========== METADATAS ==========")
    print(retrieval_results["metadatas"])

    # Step 2:
    # Extract retrieved documents

    retrieved_chunks = retrieval_results["documents"][0]

    # Step 3:
    # Extract source documents

    source_documents = []

    for metadata in retrieval_results["metadatas"][0]:

        source_documents.append(metadata["document_name"])

    # Remove duplicates (duplicate PDFs)

    source_documents = list(set(source_documents))

    # Step 4:
    # Generate final answer

    answer = generate_answer(
                              question=query,
                              retrieved_chunks=retrieved_chunks
                            )

    # Step 5:
    # Return response

    return {
             "question": query,
             "answer": answer,
             "sources": source_documents
           }