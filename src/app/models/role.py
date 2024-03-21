from src.app.app import db
from dataclasses import dataclass


@dataclass(repr=True)
class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    users = db.relationship("User", backref="role", lazy=True)
