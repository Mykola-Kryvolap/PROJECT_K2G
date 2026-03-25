import tkinter as tk

def calculate(expr):
    try:
        return str(eval(expr))
    except:
        return "Błąd"


