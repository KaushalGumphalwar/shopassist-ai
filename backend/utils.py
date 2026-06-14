import hashlib

def generate_document_hash(text):
    """
    Generate hash for document content.

    Parameters
    ----------
    text : str

    Returns
    -------
    str

    Example:
    --------
    'a8f5f167f44f4964e6c998dee827110c'
    """

    return hashlib.md5(text.encode("utf-8")).hexdigest()