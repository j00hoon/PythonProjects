from flask import Flask

app = Flask(__name__)



def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def bye():
    return "Bye~~"


if __name__ == "__main__":
    app.run(debug=True)














# import time
#
#
# current_time = time.time()
# print(current_time)
#
#
# def speed_calc_decorator(function):
#
#     def wrapper_function():
#         start_time = time.time()
#         function()
#         end_time = time.time()
#         print(f"{function.__name__} speed : {end_time - start_time}")
#
#     return wrapper_function
#
# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i
#
# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i
#
#
# fast_function()
# slow_function()



















# import time
#
# current_time = time.time()
# print(current_time)
#
#
# def speed_calc_decorator(function):
#     def wrapper_function():
#         start_time = time.time()
#         function()
#         end_time = time.time()
#         print(f"{function.__name__} run speed: {end_time - start_time}s")
#
#     return wrapper_function
#
#
# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i
#
#
# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i
#
#
# fast_function()
# slow_function()

















# Create the logging_decorator() function 👇
# def logging_decorator(function):
#     def wrapper_function(*args):
#         print(f"You called {function.__name__} function.")
#         print(f"It returned: {function(args[0], args[1], args[2])}")
#     return wrapper_function
#
#
#
# # Use the decorator 👇
# @logging_decorator
# def log_function_name(num1, num2, num3):
#     return num1 + num2 + num3
#
#
# log_function_name(1, 2, 5)