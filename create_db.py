from flask import Flask
from models import  db , Student
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()


        student1 = Student(name='Студент1', gender='Мужской', age=20, hair_color='Коричневый', eye_color='Синие')
        student2 = Student(name='Студент2', gender='Женский', age=21, hair_color='Черный', eye_color='Зеленые')
        db.session.add_all([student1, student2])
        db.session.commit()
