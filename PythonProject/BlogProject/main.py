from datetime import date

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField


## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)


##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __init__(self, title, subtitle, date, author, img_url, body):
        self.title = title
        self.subtitle = subtitle
        self.date = date
        self.author = author
        self.img_url = img_url
        self.body = body


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    # date = DateField("Date", format='%m/%d/%Y', validators=[DataRequired()])
    # date = StringField("Date", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    # body = StringField("Blog Content", validators=[DataRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


with app.app_context():
    posts = db.session.query(BlogPost).all()


@app.route('/')
def get_all_posts():
    global posts
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    # global posts
    # requested_post = None

    blog_to_see = db.session.query(BlogPost).filter_by(id=post_id).first()

    # for blog_post in posts:
    #     if blog_post["id"] == index:
    #         requested_post = blog_post
    return render_template("post.html", post=blog_to_see)


@app.route("/new", methods=["GET", "POST"])
def new_post():
    global posts
    form = CreatePostForm(meta={'csrf': False})

    if form.validate_on_submit():
        title = request.form["title"]
        subtitle = request.form["subtitle"]
        author = request.form["author"]
        img_url = request.form["img_url"]
        body = request.form["body"]
        blog_to_add = BlogPost(title, subtitle, date.today().strftime("%B %d, %Y"), author, img_url, body)
        db.session.add(blog_to_add)
        db.session.commit()

        # refresh with the new rating
        posts = db.session.query(BlogPost).all()

        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=form)


@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    global posts
    blog_to_update = db.session.query(BlogPost).filter_by(id=post_id).first()
    form = CreatePostForm(meta={'csrf': False})
    
    if form.validate_on_submit():
        blog_to_update.title = request.form["title"]
        blog_to_update.subtitle = request.form["subtitle"]
        blog_to_update.img_url = request.form["img_url"]
        blog_to_update.author = request.form["author"]
        blog_to_update.body = request.form["body"]
        db.session.commit()

        # refresh with the new rating
        posts = db.session.query(BlogPost).all()

        return redirect(url_for("get_all_posts"))
    else:
        edit_form = CreatePostForm(
            title=blog_to_update.title,
            subtitle=blog_to_update.subtitle,
            img_url=blog_to_update.img_url,
            author=blog_to_update.author,
            body=blog_to_update.body
        )

        return render_template("make-post.html", form=edit_form)


@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    global posts
    blog_to_delete = db.session.query(BlogPost).filter_by(id=post_id).first()
    db.session.delete(blog_to_delete)
    db.session.commit()

    # refresh with the new rating
    posts = db.session.query(BlogPost).all()

    return redirect(url_for("get_all_posts"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)