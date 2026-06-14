from pydantic import BaseModel


class QueryRequest(BaseModel):
    """
    User question request schema.

    Example:
    --------
    {"question": "How long does refund take?" }
    """

    question: str


class QueryResponse(BaseModel):
    """
    API response schema.

    Example:
    --------
    {
      "question": "How long does refund take?",
       "answer": "Refunds are processed within 5-7 business days.",
       "sources": ["refund_policy.txt"]
    }
    """

    question: str

    answer: str

    sources: list[str]