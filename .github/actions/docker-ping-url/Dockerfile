FROM python:alpine3.19
#WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY entrypoint.sh /entrypoint.sh

# Convert line endings to Unix style
RUN dos2unix entrypoint.sh

# Validate ENV VARs
#RUN echo "URL=$URL" 

# Set build args as env vars and execute main.py
RUN chmod +x /entrypoint.sh 
# Add a RUN directive to print directory contents
RUN ls -la /
ENTRYPOINT ["/entrypoint.sh"]

#CMD ["python", "/app/main.py"]
