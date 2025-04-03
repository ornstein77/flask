from flask import Flask
from models import Artist, Album, Song, db ,Movie,Book
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()



        artist1 = Artist(name='The Rolling Stones')
        artist2 = Artist(name='Jefferson Airplane')
        db.session.add_all([artist1, artist2])
        db.session.commit()


        album1 = Album(title='Aftermath', year='1966', artist=artist1)
        album2 = Album(title='Surrealistic Pillow', year='1967', artist=artist2)
        db.session.add_all([album1, album2])
        db.session.commit()


        song1 = Song(title='Paint it Black', length='4:20', track_number=1, album=album1)
        song2 = Song(title='White Rabbit', length='3:42', track_number=1, album=album2)
        db.session.add_all([song1, song2])
        db.session.commit()


        movie1 = Movie(title='Inception', director='Christopher Nolan', year='2010')
        movie2 = Movie(title='The Matrix', director='Lana Wachowski, Lilly Wachowski', year='1999')
        db.session.add_all([movie1, movie2])
        db.session.commit()


        book1 = Book(title='1984', author='George Orwell', year='1949')
        book2 = Book(title='Brave New World', author='Aldous Huxley', year='1932')
        db.session.add_all([book1, book2])
        db.session.commit()
