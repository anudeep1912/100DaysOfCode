from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(height=200, width=300)
window.config(padx=50, pady=50)


# Entries for Miles
entry = Entry(width=20)
# Add some text to begin with
entry.insert(END, string="")
# Gets text in entry
print(entry.get())
entry.grid(row=1, column=2)

# Label to display the converted Km.
label_km = Label(text="")
label_km.grid(row=2, column=2)
label_km.config(padx=10, pady=10)

# Label to display the Text miles.
label_m = Label(text="Miles")
label_m.grid(row=1, column=3)
label_m.config(padx=10, pady=10)

# Label to display the Text km.
label_km_text = Label(text="Kilometres")
label_km_text.grid(row=2, column=3)
label_km_text.config(padx=10, pady=10)

# Label to display is equal to
label = Label(text="Kilometres")
label.grid(row=2, column=1)
label.config(padx=10, pady=10)


# Buttons
def action():
    entered_value = float(entry.get())
    converted_value = entered_value * 1.60934
    label_km.config(text=f"{converted_value}")


# calls action() when pressed
button = Button(text="Convert", command=action)
button.grid(row=3, column=2)
button.config(padx=10, pady=10)

window.mainloop()
