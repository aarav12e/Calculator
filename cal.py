import tkinter as tk

# ----------------- Main Window -----------------
root = tk.Tk()
root.geometry("320x450")
root.overrideredirect(True)  # Remove default window border
root.configure(bg="#1e1e1e")

expression = ""

# ----------------- Functions -----------------
def press(value):
    global expression
    expression += str(value)
    screen_var.set(expression)

def equal():
    global expression
    try:
        expression = str(eval(expression))
        screen_var.set(expression)
    except:
        screen_var.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    screen_var.set("")

def close_app():
    root.destroy()

def minimize_app():
    root.iconify()

# ----------------- Title Bar -----------------
title_bar = tk.Frame(root, bg="#2c2c2c", height=35)
title_bar.pack(fill="x")

btn_close = tk.Button(title_bar, bg="#ff5f56", width=2, height=1,
                      command=close_app, bd=0)
btn_close.place(x=10, y=10)

btn_min = tk.Button(title_bar, bg="#ffbd2e", width=2, height=1,
                    command=minimize_app, bd=0)
btn_min.place(x=35, y=10)

btn_max = tk.Button(title_bar, bg="#27c93f", width=2, height=1,
                    bd=0)
btn_max.place(x=60, y=10)

# Drag window
def move_window(event):
    root.geometry(f"+{event.x_root}+{event.y_root}")

title_bar.bind("<B1-Motion>", move_window)

# ----------------- Screen -----------------
screen_var = tk.StringVar()

screen = tk.Entry(
    root,
    textvariable=screen_var,
    font=("SF Pro Display", 24),
    bg="#1e1e1e",
    fg="white",
    bd=0,
    justify="right"
)
screen.pack(fill="x", padx=20, pady=20, ipady=10)

# ----------------- Buttons -----------------
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack()

buttons = [
    ('C', clear), ('/', lambda: press('/')), ('*', lambda: press('*')), ('-', lambda: press('-')),
    ('7', lambda: press('7')), ('8', lambda: press('8')), ('9', lambda: press('9')), ('+', lambda: press('+')),
    ('4', lambda: press('4')), ('5', lambda: press('5')), ('6', lambda: press('6')), ('=', equal),
    ('1', lambda: press('1')), ('2', lambda: press('2')), ('3', lambda: press('3')), ('0', lambda: press('0')),
]

row = 0
col = 0

for text, cmd in buttons:
    tk.Button(
        btn_frame,
        text=text,
        command=cmd,
        font=("SF Pro Display", 16),
        bg="#333333" if text not in "+-*/=" else "#ff9500",
        fg="white",
        bd=0,
        width=5,
        height=2
    ).grid(row=row, column=col, padx=8, pady=8)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
