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
