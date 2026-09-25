# Choose python image to be instaled in container
FROM python:3.10-slim

# Set the working directory inside the Docker container
WORKDIR /apps

# Set environment variables to optimize Python for Docker containers(log writing)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Required py liberies will be installed from requirements.txt file(need to manually add the)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy  application code into the container-path "apps" Excepts file mentioned in .dockerignore file)
COPY . .

# Expose the port 8000 Uvicorn will run on
EXPOSE 8000

# Start the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
