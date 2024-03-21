from src.app.app import db
from dataclasses import dataclass


@dataclass(repr=True)
class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    images = db.Relationship("Image", backref="project", lazy=True)
