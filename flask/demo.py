from flask import Flask

app = Flask(__name__)

# @ => Decorator
# /first_link => is called an END POINT or API END POINT
@app.route("/first_link", methods = ['GET'])
def first_flask_function():
    print("Flask run successful")
    return "Value returned by the END point"

# EXECUTE LIKE THIS: python -m flask --app <file_name> run
if __name__ == "__main__":
    print("Hello")