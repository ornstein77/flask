from flask import Flask, render_template
from models import Artist, Album, Song, db, Movie,Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route("/songs")
def songs():

    artists_list = Artist.query.all()
    albums_list = Album.query.all()
    songs_list = Song.query.all()
    movies_list = Movie.query.all()
    books_list = Book.query.all()
    return render_template("songs.html",artists=artists_list,albums=albums_list,songs=songs_list,movies=movies_list,books=books_list)

if __name__ == '__main__':
    app.run(debug=True)