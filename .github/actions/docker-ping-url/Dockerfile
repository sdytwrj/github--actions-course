FROM python:alpine3.19
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Add input validation logic
RUN echo "URL=$URL" 
    
CMD ["python", "/app/main.py"]
