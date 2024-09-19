FROM python:3.12

WORKDIR /app

# Install the application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY . /app
EXPOSE 80

ENV NAME World

CMD ["python", "app.py", ]