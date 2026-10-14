from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(20), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    subject = db.relationship('Subject')
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
 