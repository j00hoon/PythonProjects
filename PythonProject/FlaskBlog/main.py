from flask import Flask, render_template
import requests


app = Flask(__name__)

data_url = "https://api.npoint.io/9646e11a4ce50600385a"

response = requests.get(url=data_url)
data = response.json()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/blog')
def blog():
    global data
    return render_template("index.html", data_list=data)


@app.route('/post/<blog_id>')
def get_read(blog_id):
    global data
    return render_template("post.html", data_list=data, blog_id=int(blog_id))


if __name__ == "__main__":
    app.run(debug=True)
