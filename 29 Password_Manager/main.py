from tkinter import *
from tkinter import messagebox
import random
import string

LETTERS_LOWER = [letter for letter in string.ascii_lowercase]
LETTERS_UPPER = [letter for letter in string.ascii_uppercase]
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, END)

    password_letters_lower = [random.choice(LETTERS_LOWER) for _ in range(random.randint(6, 8))]
    password_letters_upper = [random.choice(LETTERS_UPPER) for _ in range(random.randint(1, 2))]
    password_symbols = [random.choice(SYMBOLS) for _ in range(random.randint(1, 2))]
    password_numbers = [random.choice(NUMBERS) for _ in range(random.randint(1, 2))]

    password_list = password_letters_lower + password_letters_upper + password_symbols + password_numbers
    random.shuffle(password_list)
    random_generated_password = ''.join(password_list)
    password_entry.insert(END, string=random_generated_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    password_entered = password_entry.get()
    website_entered = website_entry.get()
    name_entered = name_entry.get()

    if len(website_entered) == 0 or len(password_entered) == 0:
        messagebox.showinfo("Oops", "Please don't leave any fields empty!")

    is_ok = messagebox.askokcancel(f"{website_entered}", f"These are the details entered.\n"
                                   f"Email: {name_entered}\nPassword: {password_entered}\n"
                                   "Is it ok to save?")
    if is_ok:
        password_file = open("password_data.txt", "a")
        password_file.write(f"{website_entered:25} | {name_entered:30} | {password_entered:20}\n")
        password_file.close()
        password_entry.delete(0, END)
        website_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.minsize(width=550, height=400)

# canvas to create the logo image
canvas = Canvas(width=200, height=190, highlightthickness=0)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(row=1, column=2)

# website label
website_label = Label(text="Website", width=10)
website_label.grid(row=2, column=1)
website_label.config(padx=40, pady=10)

# website entry
website_entry = Entry(width=55)
website_entry.insert(END, string="")
website_entry.grid(row=2, column=2, columnspan=2, sticky="w")
website_entry.focus()
# name label
name_label = Label(text="Username/Email", width=10)
name_label.grid(row=3, column=1)
name_label.config(padx=40, pady=10)

# name entry
name_entry = Entry(width=55)
name_entry.insert(END, string="pregadaanudeep@gmail.com")
name_entry.grid(row=3, column=2, columnspan=2, sticky="w")

# password label
password_label = Label(text="Password", width=10)
password_label.grid(row=4, column=1)
password_label.config(padx=40, pady=10)

# password entry
password_entry = Entry(width=30)

password_entry.grid(row=4, column=2, sticky="w")

# button to generate password
generate_button = Button(text="Generate Password", command=generate_password, width=15, height=1)
generate_button.grid(row=4, column=3)

# add button to add data to file
add_button = Button(text="Add", command=save_password, width=46)
add_button.grid(row=5, column=2, columnspan=2, sticky="w")


window.mainloop()
