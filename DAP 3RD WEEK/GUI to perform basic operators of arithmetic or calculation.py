import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

tk.Label(root, text="Calculator", font=("Arial", 16)).pack()

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font=("Arial", 20), justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    button_row = tk.Frame(frame)
    button_row.pack()
    for btn in row:
        button = tk.Button(button_row, text=btn, font=("Arial", 14), height=2, width=5)
        button.pack(side=tk.LEFT)
        button.bind("<Button-1>", on_click)

root.mainloop()
