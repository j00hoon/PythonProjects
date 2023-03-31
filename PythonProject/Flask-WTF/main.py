from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, DataRequired, Email
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(allow_empty_local=False)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(8, 30)])
    submit = SubmitField(label="Login")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm(meta={'csrf': False})
    if login_form.is_submitted():
        print(login_form.email.data)
        if login_form.validate():
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


@app.route("/test")
def test():
    login_form = LoginForm(meta={'csrf': False})
    return render_template("test.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)