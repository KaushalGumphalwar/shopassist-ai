"""
app.py
------

Purpose:
--------
Streamlit UI for ShopAssist AI.

Features:
---------
1. Trigger document ingestion
2. Ask questions
3. Display answers
4. Display source documents
"""

import requests
import streamlit as st

# Configuration:
API_URL = "http://localhost:8000"

# Page Configuration:
st.set_page_config(
                    page_title="ShopAssist AI",
                    page_icon="🛍️",
                    layout="wide"
                  )

st.title("🛍️ ShopAssist AI")

st.markdown("RAG-Based Customer Support System")

# Sidebar:
with st.sidebar:

    st.header("Document Management")

    if st.button("Run Document Ingestion"):

        try:

            response = requests.post(f"{API_URL}/ingest")

            result = response.json()

            st.success(result["message"])

        except Exception as e:

            st.error(str(e))

# Question Section:
st.header("Ask a Question")

question = st.text_input(
                            label="Question",
                            placeholder="Example: How long does refund take?"
                        )

# Ask Button:
if st.button("Get Answer"):
    if not question:
        st.warning("Please enter a question.")

    else:

        try:

            response = requests.post(
                                      f"{API_URL}/ask",
                                      json={"question": question}
                                    )

            result = response.json()

            st.subheader("Answer")

            st.write(result["answer"])

            st.subheader("Sources")

            for source in result["sources"]:

                st.write(f"• {source}")

        except Exception as e:

            st.error(str(e))