from src.app.app import db
from dataclasses import dataclass


@dataclass(repr=True)
class Images(db.Model):
    __tablename__ = "images"
    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.Integer, db.ForeignKey("projects.id"), nullable=False, unique=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    path = db.Column(db.String(64), index=True, unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
