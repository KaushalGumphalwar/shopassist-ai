# Use lightweight Python image to reduce image size
FROM python:3.10-slim

# Set working directory inside container
# All project files will be copied here i.e. into /app
WORKDIR /app

# Install Linux System Dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    tesseract-ocr \
    poppler-utils \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy Requirements File First (This helps Docker cache dependencies & improves Docker layer caching)
COPY requirements.txt .

# Install Python packages
# Install CPU Version of PyTorch (This avoids downloading huge NVIDIA CUDA packages)
# Reduces image size significantly
RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir \
    torch==2.8.0 \
    torchvision==0.23.0 \
    --index-url https://download.pytorch.org/whl/cpu

RUN pip install --no-cache-dir -r requirements.txt

# Copy Project Files (Copy complete project code into container)
COPY . .

# Create folders:
# Create vectorstore folder: Chroma DB data will be stored here
# Create client_docs folder: client documents will be stored here
RUN mkdir -p vectorstores
RUN mkdir -p client_docs

# Expose FastAPI & Streamlit ports
# Default FastAPI Port = 8000
# Default Streamlit Port = 8501
EXPOSE 8000
EXPOSE 8501

# Start application
# Start FastAPI + Streamlit when container runs
CMD uvicorn api.main:app --host 0.0.0.0 --port 8000 & \
    streamlit run frontend/streamlit_app.py \
    --server.address=0.0.0.0 \
    --server.port=8501