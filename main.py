import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle


def search_password():
    website = website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} found")


def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters
    shuffle(password_list)
    password = "".join(password_list)

    pass_entry.delete(0, END)
    pass_entry.insert(0, password)


def save():
    wd = website_entry.get()
    ud = user_id_entry.get()
    pd = pass_entry.get()
    new_data = {
        wd: {
            "email": ud,
            "password": pd,
        }
    }

    if len(wd) == 0 or len(pd) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
try:
    logo = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo)
except Exception:
    pass
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

user_id_label = Label(text="Email/Username:")
user_id_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

website_entry = Entry(width=25)
website_entry.grid(column=1, row=1)
website_entry.focus()

user_id_entry = Entry(width=35)
user_id_entry.grid(column=1, row=2, columnspan=2)
user_id_entry.insert(0, "ayush.koparde@gmail.com")

pass_entry = Entry(width=25)
pass_entry.grid(column=1, row=3)

gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(column=2, row=3)

search_button = Button(text="Search", width=14, command=search_password)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
