from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, Length
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe name', validators=[DataRequired(), Length(1, 30)])
    location = StringField('Cafe location on Google maps(URL)', validators=[DataRequired(), URL()])
    open_time = StringField('Opening time e.g. 8AM', validators=[DataRequired()])
    close_time = StringField('Closing time e.g. 8PM', validators=[DataRequired()])
    coffee = SelectField('Coffee rating', choices=['☕', '☕☕', '☕☕☕'])
    wifi = SelectField('Wifi strength rating', choices=['💪', '💪💪', '💪💪💪'])
    power = SelectField('Power select availability', choices=['🔌', '🔌🔌', '🔌🔌🔌'])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print(form.cafe_name.data)
        with open('cafe-data.csv', newline='', mode="a", encoding='utf8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([str(form.cafe_name.data), str(form.location.data), str(form.open_time.data),
                             str(form.close_time.data), str(form.coffee.data), str(form.wifi.data), str(form.power.data)])
        return redirect(url_for('add_cafe'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
