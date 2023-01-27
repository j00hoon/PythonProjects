import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    password_entry.delete(0, "end")

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SEARCH INFO ------------------------------- #

def search_info():
    website_input = website_entry.get()
    try:
        with open("./data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="There is no file!")
    else:
        if website_input in data:
            email = data.get(website_input).get("email")
            password = data.get(website_input).get("password")
            info = f"Website : {website_input}\n Email : {email}\n Password : {password}"
            messagebox.showinfo(title="Success to find!", message=info)
        else:
            messagebox.showerror(title="Error", message=f"There is no website name {website_input}.")
    website_entry.delete(0, "end")



# ---------------------------- UPDATE JSON ------------------------------- #


def update_json(data):

    with open("./data.json", "w") as file:
        # write new data into json
        json.dump(data, file, indent=4)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    email = email_username_entry.get()
    website = website_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email" : email,
            "password" : password,
        }
    }

    if not website and not password:
        messagebox.showerror(title="Error", message="You forgot something!")
    else:
        try:
            with open("./data.json", "r") as file:
                # read from old data
                data = json.load(file)
        except FileNotFoundError:
            update_json(new_data)
        else:
            # update old data with new data
            data.update(new_data)
            update_json(data)
        finally:
            success_info = f"Website : {website}\n Email : {email}\n Password : {password}"
            messagebox.showinfo(title="Success to insert!", message=success_info)
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")



# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password generator")
window.config(padx=50, pady=50)

# logo
logo_image = tkinter.PhotoImage(file="./logo.png")
canvas = tkinter.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# website label and entry
website_label = tkinter.Label(text="Website : ")
website_label.grid(row=1, column=0)
website_entry = tkinter.Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")

# email_username label and entry
email_username_label = tkinter.Label(text="Email/Username : ")
email_username_label.grid(row=2, column=0)
email_username_entry = tkinter.Entry(width=35)
email_username_entry.insert(0, "j00hoon1101@gmail.com")
email_username_entry.grid(row=2, column=1, columnspan=3, sticky="EW")

# password label and entry
password_label = tkinter.Label(text="Password : ")
password_label.grid(row=3, column=0)
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

# search button
search_button = tkinter.Button(text="Search", command=search_info)
search_button.grid(row=1, column=2, sticky="EW")

# generate password button
generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="EW")

# add button
add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=3, sticky="EW")



window.mainloop()




