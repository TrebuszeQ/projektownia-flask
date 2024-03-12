from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return request.headers.get('User-Agent')


if __name__ == '__main__':
    app.run(reload=True, debug=True)
