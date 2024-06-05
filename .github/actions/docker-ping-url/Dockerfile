From python:alpine3.19
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Add input validation logic
RUN echo "Validating inputs..." \
    && if [ -z "$URL" ]; then \
           echo "Error: URL input is required." \
           && exit 1 \
       fi \
    && echo "Input validation successful." && echo "URL=$URL"
    
CMD ["python", "/app/main.py"]
