FROM python:3.12

COPY . /app
# COPY before using the code
WORKDIR /app

# Install the application dependencies
RUN pip install -r requirements.txt

# Copy in the source code
CMD ["python", "app.py", ]