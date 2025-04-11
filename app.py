from flask import Flask, render_template
from flask_migrate import Migrate

from models import db, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/students")
def students():
    students_list = Student.query.all()
    return render_template("students.html", students=students_list)

if __name__ == '__main__':
    app.run(debug=True)