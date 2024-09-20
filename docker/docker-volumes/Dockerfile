FROM python:3.12

WORKDIR /app
COPY . /app
# Install the application dependencies
RUN pip install -r requirements.txt

# Copy in the source code

EXPOSE 80

ENV NAME World

CMD ["python", "app.py", ]