import json
import os

from backend.utils import (generate_document_hash)


def load_hashes(hash_file):
    """
    Load existing hashes.
    """

    if not os.path.exists(hash_file):
        return {}

    with open(hash_file, "r", encoding="utf-8") as file:
        return json.load(file)


def save_hashes(hash_file, hashes):
    """
    Save hashes.
    """

    with open(hash_file, "w", encoding="utf-8") as file:
        json.dump(hashes, file, indent=4)


def detect_changes(documents, old_hashes):
    """
    Detect updated documents.
    """

    changed_documents = []

    new_hashes = {}

    for document in documents:

        file_name = document["file_name"]

        text = document["text"]

        current_hash = (generate_document_hash(text))

        new_hashes[file_name] = current_hash

        if (file_name not in old_hashes):
            changed_documents.append(document)

        elif (old_hashes[file_name] != current_hash):
            changed_documents.append(document)

    return (changed_documents, new_hashes)