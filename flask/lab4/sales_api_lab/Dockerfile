FROM python:3.12

WORKDIR /app
COPY . /app
# Install the application dependencies
RUN pip install -r requirements.txt

ENV FLASK_APP=app.py
CMD ["python", "app.py"]