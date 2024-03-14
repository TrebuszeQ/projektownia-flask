from dataclasses import dataclass
from app.app import db


@dataclass(repr=True)
class Username(db.Model):
    __tablename__ = "usernames"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), db.ForeignKey("users.username"), unique=True, nullable=False, )
    Users = db.relationship("User", backref="username", lazy="True")
