from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, HiddenField
from wtforms.validators import DataRequired, Length
import requests



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-list.db"
db = SQLAlchemy()
db.init_app(app)


class Movie(db.Model):
    id = db.Column('Movie id', db.Integer, primary_key=True, autoincrement=True)
    title = db.Column('Movie title', db.VARCHAR(100), nullable=False)
    year = db.Column('Movie year', db.Integer, nullable=False)
    description = db.Column('Movie description', db.VARCHAR(300), nullable=False)
    rating = db.Column('Movie rating', db.Float, nullable=False)
    ranking = db.Column('Movie ranking', db.Integer, nullable=False)
    review = db.Column('Movie review', db.VARCHAR(300), nullable=False)
    img_url = db.Column('Movie URL', db.VARCHAR(100), nullable=False)

    def __init__(self, title, year, description, rating, ranking, review, img_url):
        self.title = title
        self.year = year
        self.description = description
        self.rating = rating
        self.ranking = ranking
        self.review = review
        self.img_url = img_url


class RateMovieForm(FlaskForm):
    movie_rating = FloatField('Your rating out of 10 e.g. 7.5', validators=[DataRequired()])
    movie_review = StringField('Your review', validators=[DataRequired(), Length(1, 300)])
    submit = SubmitField('Done')


class AddMovieForm(FlaskForm):
    movie_title = StringField('Movie title', validators=[DataRequired(), Length(1, 100)])
    submit = SubmitField('Done')


with app.app_context():
    db.create_all()
    # new_movie = Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )
    # db.session.add(new_movie)
    # db.session.commit()
    all_movies = db.session.query(Movie).order_by(Movie.rating).all()





@app.route("/")
def home():
    global all_movies
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    global all_movies
    form = RateMovieForm(meta={'csrf': False})
    movie_id = request.args.get('id')
    tmp_movie_update = Movie.query.get(movie_id)

    if form.validate_on_submit():
        tmp_movie_update.rating = request.form["movie_rating"]
        tmp_movie_update.review = request.form["movie_review"]
        db.session.commit()

        # refresh with the new rating
        all_movies = db.session.query(Movie).order_by(Movie.rating).all()

        return redirect(url_for("home"))

    return render_template("edit.html", movie=tmp_movie_update, form=form)


@app.route("/delete")
def delete():
    global all_movies
    movie_id = request.args.get('id')
    book_to_delete = Movie.query.get(movie_id)
    db.session.delete(book_to_delete)
    db.session.commit()

    # refresh with the new rating
    all_movies = db.session.query(Movie).order_by(Movie.rating).all()

    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    global all_movies
    form = AddMovieForm(meta={'csrf': False})

    if form.validate_on_submit():
        movie_title = request.form["movie_title"]

        movie_api = "3c2e102115c571105344a831d5120f9e"
        movie_search_url = "https://api.themoviedb.org/3/search/movie"

        response = requests.get(url=movie_search_url, params={"api_key": movie_api, "query": movie_title})
        # print(response.json()["results"])
        movies = response.json()["results"]

        return render_template("select.html", movies=movies)
    else:
        movie_title = request.args.get('movie_title')
        if movie_title is not None:
            movie_url = f"https://image.tmdb.org/t/p/w500/{request.args.get('movie_url')}"
            movie_year = request.args.get('movie_year')
            movie_review = request.args.get('movie_review')
            movie_description = request.args.get('movie_description')
            new_movie = Movie(
                title=movie_title,
                year=movie_year,
                description=movie_description,
                rating=movie_review,
                ranking=0,
                review="",
                img_url=movie_url
            )

            db.session.add(new_movie)
            db.session.commit()

            # refresh with the new rating
            all_movies = db.session.query(Movie).order_by(Movie.rating).all()

    return render_template("add.html", form=form)




if __name__ == '__main__':
    app.run(debug=True)
