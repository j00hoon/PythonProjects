import werkzeug
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DOWNLOAD_FILE'] = './static/files'
FILE_NAME = 'cheat_sheet.pdf'

Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)



##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


#Line below only required once, when creating DB. 
# db.create_all()

with app.app_context():
    users = db.session.query(User).all()



@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).filter_by(id=user_id).first()





@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        if db.session.query(User.name).filter_by(name=request.form["name"]).first() is not None:
            error="Invalid name"
            return render_template("register.html", error=error)
        if db.session.query(User.email).filter_by(email=request.form["email"]).first() is not None:
            error="Invalid email"
            return render_template("register.html", error=error)

        name = request.form["name"]
        email = request.form["email"]
        password = werkzeug.security.generate_password_hash(request.form["password"], method='pbkdf2:sha256', salt_length=8)

        user_to_add = User(name, email, password)

        db.session.add(user_to_add)
        db.session.commit()

        login_user(user_to_add)

        # user_to_auth = db.session.query(User).filter_by(email=request.form["email"], password=password)
        # login_user(user_to_auth)
        return render_template("index.html", name=name)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        if db.session.query(User.email).filter_by(email=request.form["email"]).first() is None:
            error = 'Invalid email'
            return render_template("login.html", error=error)

        user_to_login = db.session.query(User).filter_by(email=request.form["email"]).first()

        if check_password_hash(user_to_login.password, request.form["password"]):
            login_user(user_to_login)
        # return render_template("secrets.html", name=user_to_login.name)
            return redirect(url_for("secrets", name=user_to_login.name))
        else:
            error = 'Invalid password'
            return render_template("login.html", error=error)


@app.route('/secrets')
@login_required
def secrets():
    if current_user.is_authenticated:
        # return render_template("secrets.html", name=request.args.get("name"))
        return render_template("secrets.html", name=current_user.name)
    else:
        print("no")
        return render_template("index.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    if current_user.is_authenticated:
        return send_from_directory(app.config['DOWNLOAD_FILE'], FILE_NAME)
    else:
        return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
