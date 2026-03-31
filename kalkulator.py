import tkinter as tk

def calculate(expr):
    try:
        return str(eval(expr))
    except:
        return "Błąd"

def create_app():
    root = tk.Tk()
    root.title("Kalkulator")
    root.geometry("400x500")

    entry = tk.Entry(root, font=("Arial", 20), justify="right")
    entry.pack(fill="both", padx=10, pady=10)

def click(value):
        if value == "=":
            result = calculate(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)

        elif value == "C":
            entry.delete(0, tk.END)

        else:
            entry.insert(tk.END, value)

buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
        ["C"]
    ]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for btn in row:
        b = tk.Button(frame, text=btn, font=("Arial", 16))
        b.pack(side="left", expand=True, fill="both")
        b.config(command=lambda t=btn: click(t))
