import tkinter as tk

def on_button_click(button_value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(button_value))

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("QASCalculator")

# Configure the window background
window.configure(bg="black")

# Entry widget for displaying and entering numbers
entry = tk.Entry(window, width=20, font=("Arial", 14), bg="black", fg="lime green")
entry.grid(row=0, column=0, columnspan=4)

# Define buttons and their positions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create buttons and add them to the grid
for (text, row, col) in buttons:
    button = tk.Button(window, text=text, width=5, height=2, command=lambda t=text: on_button_click(t), bg="black", fg="lime green")
    button.grid(row=row, column=col)

# Configure the "=" button to calculate the result
equal_button = window.grid_slaves(row=4, column=2)[0]
equal_button.configure(command=calculate)

# Configure the "C" button to clear the entry
clear_button = window.grid_slaves(row=4, column=1)[0]
clear_button.configure(command=clear)

# Run the main loop
window.mainloop()
