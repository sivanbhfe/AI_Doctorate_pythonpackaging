from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_word():
    return "Hello this is pytest testing"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5001)