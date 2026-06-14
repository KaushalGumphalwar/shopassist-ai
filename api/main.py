from fastapi import FastAPI

from api.schemas import (QueryRequest, QueryResponse)

from backend.ingestion_pipeline import (run_ingestion)

from backend.rag_pipeline import (ask_question)


# Create FastAPI App:
app = FastAPI(
               title="ShopAssist AI",
               description="RAG-Based Customer Support System",
               version="1.0.0"
             )

# Test API:
@app.get("/")
def home():
    """
    Health check endpoint.
    """

    return {"message": "ShopAssist AI API is running"}

# Document Ingestion API:
@app.post("/ingest")
def ingest_documents():
    """
    Run document ingestion pipeline.

    Pipeline:
    ---------
    Load Documents
           ↓
    Chunking
           ↓
    Embeddings
           ↓
    ChromaDB Storage
    """

    try:
        run_ingestion()
        return {
                 "status": "success",
                 "message": "Documents ingested successfully"
               }
    
    except Exception as e:
        return {
                 "status": "error",
                 "message": str(e)
               }

# Ask Question API:
@app.post("/ask", response_model=QueryResponse)
def ask(request: QueryRequest):
    """
    Ask question to RAG system.
    """

    response = ask_question(request.question)

    return QueryResponse(
                          question=response["question"],
                          answer=response["answer"],
                          sources=response["sources"]
                        )