from dataclasses import dataclass
from src.app.app import db


@dataclass(repr=True)
class Email(db.Model):
    __tablename__ = "emails"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), db.ForeignKey("users.id"), unique=True, nullable=False)
    users = db.relationship("User", backref="email", lazy=True)
