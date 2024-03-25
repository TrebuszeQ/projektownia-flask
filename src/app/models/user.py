from app import db
from dataclasses import dataclass


@dataclass(repr=True)
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), db.ForeignKey("usernames.id"), unique=True, nullable=False, index=True)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), db.ForeignKey("emails.id"), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
