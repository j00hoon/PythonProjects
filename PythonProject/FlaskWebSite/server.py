from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def initial_page():
    random_number = random.randint(1, 10)
    today = datetime.date.today()
    current_year = today.year
    return render_template("index.html", num=random_number, CURRENT_YEAR=current_year, MY_NAME="Seunghoon Baik")


@app.route("/guess/<name>")
def guess_gender_age(name):
    gender_url = f"https://api.genderize.io?name={name}"
    age_url = f"https://api.agify.io?name={name}"

    response = requests.get(url=gender_url)
    gender = response.json()["gender"]

    response = requests.get(url=age_url)
    age = response.json()["age"]

    return render_template("guess.html", NAME=name, GENDER=gender, AGE=age)


@app.route("/blog/<random_number>")
def get_blog(random_number):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"

    response = requests.get(url=blog_url)
    all_data = response.json()
    random_number = random_number

    return render_template("blog.html", blog_data=all_data, random_number=random_number)


if __name__ == "__main__":
    app.run(debug=True)