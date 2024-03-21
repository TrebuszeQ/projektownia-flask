from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import tomllib
import os


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.from_file("../properties.toml", load=tomllib.load, text=False)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run(debug=True)
