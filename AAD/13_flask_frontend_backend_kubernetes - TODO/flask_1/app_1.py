from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

@app.route("/flask1")
def home():
    return jsonify(message="Welcome to flask 1 App")

# EndPoint with @ decorator
@app.route("/communicate")
def communicate ():
    response = requests.get("http://flask-app-2:5000/flask2")
    return response.json()
 
if __name__== "__main__":
    # With app.run, you can directly run this as a python script
    app.run(host = '0.0.0.0' , debug=True)

# Running the app
# RUNNING THE APP: python -m flask --app flask/lab1_quickstart.py run
# RUNNING APP OVER WEB: python -m flask --app flask/lab1_quickstart.py run --host=0.0.0.0
# GETTING DATA FROM JSON: curl http://127.0.0.1:5000/getname -H "Content-Type:application/json" -d '{"Name": "ajinkya"}'