FROM python:3.12

COPY . /app
WORKDIR /app
# Install the application dependencies
RUN pip install -r requirements.txt

# Copy in the source code

EXPOSE 80

CMD ["python", "app.py", ]