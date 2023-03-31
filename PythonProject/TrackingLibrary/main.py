from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book-collection.db"
db = SQLAlchemy()
db.init_app(app)



class AddBookForm(FlaskForm):
    # book_id = IntegerField('Book id', validators=[DataRequired()])
    book_name = StringField('Book name', validators=[DataRequired(), Length(1, 30)])
    book_author = StringField('Book author', validators=[DataRequired(), Length(1, 30)])
    # book_rating = SelectField('Book rating', choices=['📚', '📚📚', '📚📚📚'])
    book_rating = FloatField('Book rating', validators=[DataRequired()])
    submit = SubmitField('Submit')



class Book(db.Model):
    id = db.Column('Book id', db.Integer, primary_key=True, autoincrement=True)
    title = db.Column('Book title', db.VARCHAR(250), nullable=False)
    author = db.Column('Book author', db.VARCHAR(250), nullable=False)
    rating = db.Column('Book rating', db.Float, nullable=False)


    def __init__(self, title, author, rating):
        # self.id = id
        self.title = title
        self.author = author
        self.rating = rating



with app.app_context():
    db.create_all()
    all_books = db.session.query(Book).all()







@app.route('/')
def home():
    global all_books
    # print(all_books)
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    global all_books

    form = AddBookForm(meta={'csrf': False})

    if request.method == "GET":
        return render_template("add.html", form=form)
    else:
        tmp_dic = {
            # "id" : form.book_id,
            "title" : form.book_name.data,
            "author" : form.book_author.data,
            "rating" : form.book_rating.data
        }
        all_books.append(tmp_dic)
        added_book = Book(form.book_name.data, form.book_author.data, form.book_rating.data)

        with app.app_context():
            db.session.add(added_book)
            db.session.commit()
            # try:
            #     db.session.add(added_book)
            #     db.session.commit()
            # except sqlite3.OperationalError:
            #     db.create_all()
            #     db.session.add(added_book)
            #     db.session.commit()

        return redirect(url_for("home"))


@app.route("/edit_rating", methods=["GET", "POST"])
def edit_rating():
    global all_books

    if request.method=="GET":
        tmp_book=Book.query.filter_by(title=request.args.get('title'), author=request.args.get('author'), rating=request.args.get('rating')).first()

        return render_template("edit.html", book=tmp_book)
    else:
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating_number"]
        db.session.commit()

        # refresh with the new rating
        all_books = db.session.query(Book).all()

        return redirect(url_for("home"))


@app.route("/delete")
def delete():
    global all_books

    book_id = request.args.get("book_id")
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

    # refresh with the new rating
    all_books = db.session.query(Book).all()

    return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(debug=True)

