from flask import Flask, request
import tomllib
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_file("/src/properties.toml", load=tomllib.load, text=False)
db = SQLAlchemy(app)


@app.route('/')
def hello_world():  # put application's code here
    return request.headers.get('User-Agent')


if __name__ == '__main__':
    app.run(debug=True)
