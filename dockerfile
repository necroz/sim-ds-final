# Use a lightweight Python base image
FROM python:3.10.12-slim

# Set the working directory inside the container
WORKDIR /

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the FastAPI app will run on
EXPOSE 8000

# Command to run the FastAPI application with Uvicorn
# Use the exec form for proper signal handling
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]