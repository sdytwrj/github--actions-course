FROM python:alpine3.19
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Validate ENV VARs
#RUN echo "URL=$URL" 

# Set build args as env vars and execute main.py
RUN chmod +x entrypoint.sh 
ENTRYPOINT ["/app/entrypoint.sh"]

#CMD ["python", "/app/main.py"]
