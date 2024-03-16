from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Password Generator Project
def generate_pass():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
	           'v',
	           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
	           'R',
	           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	password_letters = [choice(letters) for _ in range(randint(8, 10))]
	password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
	password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

	password_list = password_numbers + password_symbols + password_letters
	shuffle(password_list)

	password = "".join(password_list)
	password_entry.insert(END, password)
	messagebox.showinfo(title="Successfull", message="Your information saved and new password copied to clipboard.")
	pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_data():
	website = web_entry.get()
	email = user_entry.get()
	password = password_entry.get()
	new_data = {
		website:{
			"email" : email,
			"password" : password,
		}
	}

	if len(website) == 0 or len(password) == 0:
		messagebox.showinfo(title="Something went wrong !", message="Please fill the all related fields")
	else:
		try:
			with open("data.json", "r") as data_file:
				data = json.load(data_file)

		except:
			with open("data.json", "w") as data_file:
				json.dump(new_data, data_file, indent=4)

		else:
			data.update(new_data)

			with open("data.json", "w") as data_file:
				json.dump(data, data_file, indent=4)

		finally:
			web_entry.delete(0, END)
			password_entry.delete(0, END)

def find_password():
	website = web_entry.get()

	try:
		with open("data.json", "r") as search_dict:
			data = json.load(search_dict)
	except FileNotFoundError:
		messagebox.showinfo(title="File Not Found", message= " No Data File Found")
	else:
		if website in data:
			email = data[website]["email"]
			password = data[website]["password"]
			messagebox.showinfo(title=f"{website} / {email}" , message=f"Yor password for {website}/{email} is {password} and copied to clipboard.")
			pyperclip.copy(password)
		else:
			messagebox.showinfo(title="Data Not Found", message="No details for the website exist")




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=0, row=1, columnspan=3)

website_text = Label(text="Website:")
website_text.grid(sticky=W, column=0, row=2, padx=1, pady=1)

user_text = Label(text="Email/Username:")
user_text.grid(sticky=W, column=0, row=3, padx=1, pady=1)

password_text = Label(text="Password:")
password_text.grid(sticky=W, column=0, row=4, padx=1, pady=1)

web_entry = Entry(width=40)
web_entry.grid(sticky=W, column=1, row=2, columnspan=2, padx=1, pady=1)
web_entry.focus()

user_entry = Entry(width=40)
user_entry.insert(END, "name.surname@somemail.com")
user_entry.grid(sticky=W, column=1, row=3, columnspan=2, padx=1, pady=1)

password_entry = Entry(width=40)
password_entry.grid(sticky=W, column=1, row=4, columnspan=2, padx=1, pady=1)

password_button = Button(text="Generate Password", highlightthickness=0, width=16, command=generate_pass)
password_button.grid(sticky=W, column=1, row=5, padx=2, pady=2)

add_button = Button(text="Add", highlightthickness=0, width=16, command=add_data)
add_button.grid(sticky=W, column=2, row=5, padx=2, pady=2)

search_button = Button(text="Search", highlightthickness=0, width=34, command=find_password)
search_button.grid(sticky=W, column=1, row=6, padx=2, pady=2, columnspan=2)

window.mainloop()
