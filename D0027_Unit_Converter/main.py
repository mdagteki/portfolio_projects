from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=10, pady=20)

miles = Label(text="Miles", font=("Arial", 12, "bold"))
miles.place(x=200, y=0)

km = Label(text="Km", font=("Arial", 12, "bold"))
km.place(x=200, y=50)

equal = Label(text="is equal to", font=("Arial", 12, "bold"))
equal.place(x=0, y=50)

m_text = Entry(width=13, justify="left")
m_text.place(x=100, y=0)

k_text = Text(height=1, width=10)
k_text.place(x=100, y=50)


def calculate():
	m = int(m_text.get())
	k = m * 1.60934
	k_text.insert(END, str(round(k, 2)))


button = Button(text="Convert", font=("Arial", 12, "bold"), command=calculate)
button.place(x=100, y=100)

window.mainloop()
