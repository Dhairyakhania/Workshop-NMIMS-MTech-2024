from flask import Flask, request

app = Flask(__name__)

@app.route("/getmean", methods=["GET"])
def get_mean():
    data = request.get_json()
    number_1 = int(data['num1'])
    number_2 = int(data['num2'])
    return str((number_1 + number_2 )/2)

@app.route("/getmax", methods = ['GET'])
def get_max():
    # Alternative to request.get_json
    # data = request.get_json()
    # number_1 = int(data['num1'])
    # number_2 = int(data['num2'])
    number_1 = int(request.args.get("num1"))
    number_2 = int(request.args.get("num2"))
    return str(max(number_1, number_2))
    # can call with http://127.0.0.1:5000/getmax?num1=10&num2=20 too

if __name__== "__main__":
    app.run(debug=True)

# RUNNING THE APP: python -m flask --app flask/quickstart.py run
# RUNNING APP OVER WEB: python -m flask --app flask/quickstart.py run --host=0.0.0.0
# GETTING DATA FROM JSON: curl http://127.0.0.1:5000/getname -H "Content-Type:application/json" -d '{"Name": "ajinkya"}'