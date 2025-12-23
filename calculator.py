import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry box
expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

equation = tk.StringVar()

entry = tk.Entry(
    root,
    textvariable=equation,
    font=("Arial", 20),
    bd=10,
    relief="ridge",
    justify="right"
)
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Buttons frame
frame = tk.Frame(root)
frame.pack()

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

for (text, row, col) in buttons:
    tk.Button(
        frame,
        text=text,
        width=5,
        height=2,
        font=("Arial", 16),
        command=lambda t=text: equal() if t == '=' else press(t)
    ).grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(
    root,
    text="C",
    font=("Arial", 16),
    bg="red",
    fg="white",
    command=clear
).pack(fill="both", padx=10, pady=10)

root.mainloop()
