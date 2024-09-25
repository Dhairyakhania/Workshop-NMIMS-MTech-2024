FROM python:3.12

WORKDIR /app
COPY . /app
# Install the application dependencies
RUN pip install -r requirements.txt

# Copy in the source code
CMD ["python", "app.py", ]