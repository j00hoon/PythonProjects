from functools import wraps

import werkzeug
from flask import Flask, render_template, redirect, url_for, flash, request, g, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

from flask_wtf import FlaskForm
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from wtforms import StringField, validators, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, URL

from forms import CreatePostForm
from flask_gravatar import Gravatar
from forms import CommentForm






ADMIN_ID = 1

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)


login_manager = LoginManager()
login_manager.init_app(app)





##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)








##CONFIGURE TABLES
class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="author")

    # def __init__(self, name, email, password):
    #     self.name = name
    #     self.email = email
    #     self.password = password



class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # author = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    author = relationship("User", lazy='subquery', back_populates="posts")
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    comments = relationship("Comment", back_populates="parent_post")

    # def __init__(self, title, subtitle, date, img_url, body):
    #     self.title = title
    #     self.subtitle = subtitle
    #     self.date = date
    #     # self.author = author
    #     self.img_url = img_url
    #     self.body = body


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String(500))

    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    author = relationship("User", lazy='subquery', back_populates="comments")

    blog_id = db.Column(db.Integer, ForeignKey('blog_posts.id'))
    parent_post = relationship("BlogPost", lazy='subquery', back_populates="comments")



# Create user form
class CreateUserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(max=60), validators.Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=20)])
    submit = SubmitField("Create User")


# Login form
class LoginUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(max=60), validators.Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=20)])
    submit = SubmitField("Login")


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


#Create login-required decorator
def login_required(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        if current_user.is_authenticated:
            return function(*args, **kwargs)
        return abort(403)
    return wrapper_function


#Create admin-only decorator
def admin_only(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        if current_user.id != ADMIN_ID:
            return abort(403)
        return function(*args, **kwargs)
    return wrapper_function


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).filter_by(id=user_id).first()


















@app.route('/')
def get_all_posts():
    # posts = BlogPost.query.all()
    global posts, ADMIN_ID

    if str(ADMIN_ID) == request.args.get("user_id"):
        return render_template("index.html", all_posts=posts, ADMIN=True)
    return render_template("index.html", all_posts=posts, ADMIN=False)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = CreateUserForm(meta={'csrf': False})

    if request.method=="GET":
        return render_template("register.html", form=form)
    else:
        if db.session.query(User.name).filter_by(name=request.form["name"]).first() is not None:
            error="Invalid name"
            return render_template("register.html", error=error, form=form)
        if db.session.query(User.email).filter_by(email=request.form["email"]).first() is not None:
            error="Invalid email"
            return render_template("register.html", error=error, form=form)

        password = werkzeug.security.generate_password_hash(request.form["password"], method='pbkdf2:sha256', salt_length=8)

        user_to_add = User(
            name=form.name.data,
            email=form.email.data,
            password=password
        )

        db.session.add(user_to_add)
        db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route('/login', methods=["GET", "POST"])
def login():
    global posts
    form = LoginUserForm(meta={'csrf': False})

    if form.validate_on_submit():
        email = request.form["email"]
        password = request.form["password"]

        if db.session.query(User.email).filter_by(email=email).first() is None:
            error = 'Invalid email'
            return render_template("login.html", error=error, form=form)

        user_to_login = db.session.query(User).filter_by(email=email).first()

        if check_password_hash(user_to_login.password, password):
            login_user(user_to_login)
            return redirect(url_for("get_all_posts", user_id=user_to_login.id))
        else:
            error = 'Invalid password'
            return render_template("login.html", error=error, form=form)
    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
@login_required
@admin_only
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    form = CommentForm()

    if form.validate_on_submit():
        # comment = request.form["comment"]
        new_comment = Comment(
            comment=request.form["comment"],
            user_id=current_user.id,
            blog_id=post_id
        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("post.html", post=requested_post, form=form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post", methods=["GET", "POST"])
@login_required
@admin_only
def add_new_post():
    global posts

    form = CreatePostForm(meta={'csrf': False})

    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()

        # refresh with the new rating
        posts = db.session.query(BlogPost).all()

        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>")
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))













with app.app_context():
    db.create_all()
    posts = db.session.query(BlogPost).all()
    users = db.session.query(User).all()



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
