import tkinter as tk

# Function to handle button clicks
def on_button_click(value):
    current_text = expression.get()
    if current_text == "0":
        expression.set(str(value))
    else:
        expression.set(current_text + str(value))

# Function to clear the display
def clear_display():
    expression.set("0")

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(expression.get())
        expression.set(str(result))
    except Exception:
        expression.set("Error")

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x600")
root.configure(bg="#578c7b")
root.resizable(False, False)

# StringVar to hold the expression
expression = tk.StringVar()
expression.set("0")

# Entry widget to display the expression/result
display = tk.Entry(root, textvariable=expression, font=("Courier New", 24), bd=0, bg="white", justify="right")
display.pack(expand=True, fill="both", padx=10, pady=20)

# Define the buttons in a list of lists
buttons = [
    ['C', '', '', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=', '']
]

# Create and place the buttons
for row in buttons:
    row_frame = tk.Frame(root, bg="#578c7b")
    row_frame.pack(expand=True, fill="both")
    for btn_text in row:
        if btn_text == '':
            # Empty placeholder
            tk.Label(row_frame, text='', bg="#578c7b").pack(side="left", expand=True, fill="both", padx=5, pady=5)
        else:
            # Determine the command based on the button text
            if btn_text == 'C':
                command = clear_display
            elif btn_text == '=':
                command = evaluate_expression
            else:
                command = lambda val=btn_text: on_button_click(val)
            # Create the button
            tk.Button(
                row_frame,
                text=btn_text,
                font=("Courier New", 20),
                fg="black",
                bg="lightgreen" if btn_text in ['+', '-', '*', '/', '=', 'C'] else "lightgray",
                bd=0,
                command=command
            ).pack(side="left", expand=True, fill="both", padx=5, pady=5)

# Run the application
root.mainloop()