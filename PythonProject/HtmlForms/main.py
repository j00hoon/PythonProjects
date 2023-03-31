from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def initial_page():
    return render_template("index.html")


@app.route("/login-receive-data", methods=["POST"])
def login_receive_data():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    # return render_template("login.html", username=username, password=password)
    return f"<h1>Name : {username} Password : {password}</h1>"


@app.route("/contact", methods=["GET", "POST"])
def contact_route():
    if request.method == 'GET':
        return contact_input_page()
        # return render_template("contact.html")
    elif request.method == 'POST':
        return contact_receive_data()


@app.route("/contact-input-page", methods=["GET"])
def contact_input_page():
    return render_template("contact.html", inputOrSuccess=None)


@app.route("/contact-receive-data", methods=["POST"])
def contact_receive_data():
    fullname = request.form["fullname"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]

    print(f"Fullname : {fullname}\nEmail : {email}\nPhone : {phone}\nMessage : {message}")
    # return "<h1>Successfully sent your message</h1>"
    return render_template("contact.html", fullname=fullname, email=email, phone=phone, message=message)


if __name__ == "__main__":
    app.run(debug=True)