from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///my-books-collection.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


@app.route('/')
def home():
    # Home Page
    all_books = Book.query.all()
    return render_template('index.html', book_list=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    # Add a new Book to data base
    if request.method == 'POST':
        new_book = Book(title=request.form['book'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit", methods=['POST', 'GET'])
def edit():
    # Edit the rating of a current book
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template('edit_rating.html', book=book_selected)


@app.route("/delete")
def delete():
    # Delete a book from data base
    book_id = request.args.get('id')
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
