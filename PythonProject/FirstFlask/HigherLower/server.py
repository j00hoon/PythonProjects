from flask import Flask
import random

app = Flask(__name__)

target_number = random.randint(0, 9)
print(target_number)


# def find_target_number(function):
#     global target_number
#
#     def wrapper(*args):
#         if function(args[0]) < target_number:
#             return "<h1>Too low, try again!</h1>" \
#                    "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
#         elif function(args[0]) > target_number:
#             return "<h1>Too high, try again!</h1>" \
#                    "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
#         else:
#             return "<h1>Correct!</h1>" \
#                    "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
#     return wrapper


@app.route("/")
def initial_game_screen():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<number>")
def guess_number(number):
    global target_number

    if int(number) < target_number:
        return "<h1>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif int(number) > target_number:
        return "<h1>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1>Correct!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)