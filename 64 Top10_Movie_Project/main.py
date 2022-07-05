from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
import os

MOVIE_DB_API_KEY = os.getenv('MOVIE_DB_API_KEY')
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top_10_movies.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(500), nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


class EditForm(FlaskForm):
    # A form Object inheriting from WTForms
    rating = StringField('Your Rating out of 10 E.g. 7.5', validators=[DataRequired()], render_kw={"style": "font-weight: bold;"})
    review = StringField('Your Review.', validators=[DataRequired()], render_kw={"style": "font-weight: bold;"})
    submit = SubmitField('Done')


class AddForm(FlaskForm):
    # A form Object inheriting from WTForms
    title = StringField('Title', validators=[DataRequired()], render_kw={"style": "font-weight: bold;"})
    submit = SubmitField('Add Movie')


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
        db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    edit_form = EditForm()
    if edit_form.validate_on_submit():
        new_data = edit_form.data
        movie_id = request.args.get("id")
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = new_data["rating"]
        movie_to_update.review = new_data["review"]
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=edit_form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        movie_title = add_form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=add_form)


@app.route("/find", methods=['GET', 'POST'])
def find():
    movie_id = request.args.get("id")
    if movie_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_id}"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
