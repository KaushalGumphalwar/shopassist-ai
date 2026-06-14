import google.generativeai as genai

from backend.config import (GEMINI_API_KEY, GEMINI_MODEL)


# Configure Gemini:

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(GEMINI_MODEL)


def generate_answer(question, retrieved_chunks):
    """
    Generate final answer.

    Parameters
    ----------
    question : str

    retrieved_chunks : list

    Example:
    --------
    [
        "Refunds are processed within 5-7 business days.",
        "Refund status can be tracked from Orders section."
    ]

    Returns
    -------
    str
    """

    # Combine retrieved chunks

    context = "\n\n".join(retrieved_chunks)

    # Prompt

    prompt = f"""
                You are an E-Commerce Customer Support Assistant.

                Answer the user's question only using the provided context.

                If the answer is not available in the context, respond with:

                "I could not find this information in the provided documents."

                Context:
                {context}

                Question:
                {question}
                """

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        print("\nGEMINI ERROR:")
        print(e)

        fallback_response = (
                              "Gemini is currently unavailable.\n\n"
                              "Relevant information found:\n\n"
                              f"{context}"
                            )

        return fallback_response