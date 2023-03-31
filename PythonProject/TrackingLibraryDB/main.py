# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
#
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()




from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy()
db.init_app(app)


class bookss(db.Model):
   id = db.Column('book_id', db.Integer, primary_key = True)
   title = db.Column(db.VARCHAR(250), nullable=False)
   author = db.Column(db.VARCHAR(250), nullable=False)
   rating = db.Column(db.Float, nullable=False)

   def __init__(self, id, title, author, rating):
       self.id = id
       self.title = title
       self.author = author
       self.rating = rating


data = bookss(1, 'Harry potter', 'J.K.Rowling', 9.3)

with app.app_context():
    db.create_all()
    # db.session.add(data)
    # db.session.commit()