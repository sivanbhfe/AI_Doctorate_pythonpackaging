from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello from CI/CD power by Flask AP"

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1")

