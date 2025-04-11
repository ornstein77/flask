from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()





class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String(50), nullable=False)
    eye_color = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Student {self.name}>'



