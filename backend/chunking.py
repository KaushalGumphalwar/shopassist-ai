from langchain.text_splitter import (RecursiveCharacterTextSplitter)

from backend.config import (CHUNK_SIZE, CHUNK_OVERLAP)


def create_chunks(documents):
    """
    Convert documents into chunks.

    Parameters
    ----------
    documents : list

    Example:
    --------
    [
        {
            "file_name": "faq.txt",
            "text": "Frequently Asked Questions..."
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
            "chunk_text": "Frequently Asked Questions..."
        }
    ]
    """

    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)

    all_chunks = []

    for document in documents:

        print(
               f"\n{document['file_name']} "
               f"Length = {len(document['text'])}"
             )

        chunks = splitter.split_text(document["text"])

        print(f"Chunks Created = {len(chunks)}")

        for index, chunk in enumerate(chunks):

            all_chunks.append(
                                {
                                    "chunk_id": f"{document['file_name']}_{index}",

                                    "document_name": document["file_name"],

                                    "chunk_text": chunk
                                }
                             )

    return all_chunks