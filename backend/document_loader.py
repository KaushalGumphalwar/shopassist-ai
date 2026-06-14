import os

from unstructured.partition.pdf import partition_pdf

from backend.config import DATA_FOLDER

def load_documents():
    """
    Load all documents from DATA_FOLDER.

    Returns
    -------
    list

    Example:
    --------
    [
        {
            "file_name": "faq.txt",
            "text": "Frequently Asked Questions..."
        },
        {
            "file_name": "refund_policy.txt",
            "text": "Refund Policy..."
        }
    ]
    """

    documents = []

    # Loop through all files (This file reads all documents from: DATA_FOLDER = "client_docs")
    for file_name in os.listdir(DATA_FOLDER):

        file_path = os.path.join(DATA_FOLDER, file_name)

        # Skip directories
        if not os.path.isfile(file_path):
            continue

        try:

            # Extract content using unstructured (This file uses partition_text() to extract text)
            elements = partition_pdf(filename=file_path)

            print(f"\nFILE: {file_name}")
            print(f"ELEMENTS COUNT: {len(elements)}")

            for e in elements[:3]:
                print("ELEMENT TEXT:", repr(getattr(e, "text", None)))

            text = "\n".join(element.text for element in elements if getattr(element, "text", None))

            print("FINAL TEXT LENGTH:", len(text))
            print("FINAL TEXT SAMPLE:", repr(text[:100]))
                                        
            documents.append(
                                {
                                    "file_name": file_name,
                                    "text": text
                                }
                            )

        except Exception as e:

            print(f"Error loading {file_name}: {e}")

    return documents  # Returns all documents as a list.