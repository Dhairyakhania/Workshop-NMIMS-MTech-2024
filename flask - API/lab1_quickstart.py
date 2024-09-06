from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/first")
def hello_world2():
    return "<p>/first path</p>"

# EndPoint with @ decorator
@app.route("/getname", methods = ['GET', 'POST'])
def get_name():
    data = request.get_json()
    return data


if __name__== "__main__":
    app.run(debug=True)

# RUNNING THE APP: python -m flask --app flask/quickstart.py run
# RUNNING APP OVER WEB: python -m flask --app flask/quickstart.py run --host=0.0.0.0
# GETTING DATA FROM JSON: curl http://127.0.0.1:5000/getname -H "Content-Type:application/json" -d '{"Name": "ajinkya"}'