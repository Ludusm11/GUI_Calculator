import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Function to evaluate and display the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Function to append numbers or operators to the entry
def append_to_entry(value):
    entry.insert(END, value)

# Function to clear the entry field
def clear_entry():
    entry.delete(0, END)

# Initialize the main window
root = ttk.Window(themename="superhero")
root.title("Calculator")
root.geometry("300x400")

# Entry widget for displaying the expression and result
entry = ttk.Entry(root, font=("Helvetica", 20), justify="right")
entry.pack(pady=20, fill=X, padx=10)

# Button frame
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
]

# Create buttons and add them to the grid
for row_index, row in enumerate(buttons):
    for col_index, button_text in enumerate(row):
        if button_text == "=":
            btn = ttk.Button(button_frame, text=button_text, command=calculate, bootstyle=SUCCESS)
        else:
            btn = ttk.Button(button_frame, text=button_text, command=lambda txt=button_text: append_to_entry(txt))
        btn.grid(row=row_index, column=col_index, padx=5, pady=5, ipadx=10, ipady=10)

# Clear button
clear_button = ttk.Button(root, text="Clear", command=clear_entry, bootstyle=DANGER)
clear_button.pack(pady=10, ipadx=80)

# Run the main loop
root.mainloop()
