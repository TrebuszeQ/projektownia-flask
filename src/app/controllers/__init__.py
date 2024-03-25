from dataclasses import dataclass

from app import app, db


@app.route('/user', methods=["GET", "POST"])
@dataclass(repr=True)
class UserController:
    pass