FROM python:alpine3.19
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Set build args as env vars
ENTRYPOINT ["/app/entrypoint.sh"]

# Validate ENV VARs
RUN echo "URL=$URL" 

CMD ["python", "/app/main.py"]
