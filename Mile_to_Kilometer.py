from tkinter import *


def mile_input():
    miles = float(miles_entry.get())
    km = round(miles * 1.609)
    label3.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Convertor")
window.config(padx=20, pady=20)

miles_entry = Entry(width=10)
miles_entry.grid(row=0, column=1)

label1 = Label(text="Miles")
label1.grid(row=0, column=2)
label1.config(padx=3, pady=3)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)
label2.config(padx=3, pady=3)

label3 = Label(text="0")
label3.grid(row=1, column=1)
label3.config(padx=3, pady=3)

label4 = Label(text="Km")
label4.grid(row=1, column=2)
label4.config(padx=3, pady=3)

button = Button(text="Calculate", command=mile_input)
button.grid(row=2, column=1)
label1.config(padx=3, pady=3)

window.mainloop()
