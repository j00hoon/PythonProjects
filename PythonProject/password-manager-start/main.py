import tkinter
from tkinter import messagebox
import random
import pyperclip


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

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    email = email_username_entry.get()
    website = website_entry.get()
    password = password_entry.get()

    if not website and not password:
        messagebox.showerror(title="Error", message="You forgot something!")
    else:
        is_ok = messagebox.askyesno(title="Confirmation", message=f"These are the details entered: \nWebsite: {website} " f"\nEmail: {email}" f"\nPassword: {password}")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
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
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")

# email_username label and entry
email_username_label = tkinter.Label(text="Email/Username : ")
email_username_label.grid(row=2, column=0)
email_username_entry = tkinter.Entry(width=35)
email_username_entry.insert(0, "j00hoon1101@gmail.com")
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

# password label and entry
password_label = tkinter.Label(text="Password : ")
password_label.grid(row=3, column=0)
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

# generate password button
generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="EW")

# add button
add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")



window.mainloop()




