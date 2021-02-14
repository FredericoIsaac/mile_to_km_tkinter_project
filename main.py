from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)


def calculate():
    miles = float(entry_miles.get())
    miles_to_km = miles * 1.609344
    label_to_km.config(text=f"{round(miles_to_km)}")


entry_miles = Entry(width=10)
entry_miles.insert(END, string="0")
entry_miles.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_text_0 = Label(text="is equal to")
label_text_0.grid(column=0, row=1)

label_to_km = Label(text="0")
label_to_km.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

button_calculate = Button(text="Calculate", command=calculate)
button_calculate.grid(column=1, row=2)


window.mainloop()
