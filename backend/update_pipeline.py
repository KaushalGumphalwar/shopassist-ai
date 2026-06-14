from backend.config import (HASH_FILE)

from backend.document_loader_old import (load_documents)

from backend.document_tracker import (load_hashes, save_hashes, detect_changes)

from backend.chunking import (create_chunks)

from backend.embeddings import (generate_embeddings)

from backend.vectorstore import (delete_document_vectors, store_chunks)


def run_update_pipeline():

    # Step 1
    # Load documents

    documents = load_documents()

    # Step 2
    # Load previous hashes

    old_hashes = load_hashes(HASH_FILE)

    # Step 3
    # Detect changes

    (changed_documents, new_hashes) = detect_changes(documents, old_hashes)

    if not changed_documents:

        print("No document updates found.")

        return

    # Step 4
    # Process changed docs only

    for document in changed_documents:

        file_name = document["file_name"]

        print(f"Updating {file_name}")

        # Delete old vectors

        delete_document_vectors(file_name)

        # Create chunks

        chunks = create_chunks([document])

        # Create embeddings

        chunks = (generate_embeddings(chunks))

        # Store new vectors

        store_chunks(chunks)

    # Step 5
    # Save latest hashes

    save_hashes(HASH_FILE, new_hashes)

    print("Update completed.")