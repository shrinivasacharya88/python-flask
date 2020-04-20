from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World! this is test from today 20th 2020 and now deployment in kubernaties this is my first cicd this include mail"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
