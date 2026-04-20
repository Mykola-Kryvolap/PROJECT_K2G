import math
from historia import add

def calculate(expr):
    try:
        expr = expr.replace("^", "**")
        expr_clean = expr.replace(" ", "")

        for op in ["+", "-", "*", "/"]:
            if op in expr_clean and expr_clean.endswith("%"):
                parts = expr_clean.split(op, 1)
                if len(parts) == 2 and parts[1].endswith("%"):
                    a_val = float(parts[0])
                    percent = float(parts[1][:-1])
                    if op == "+":
                        result = a_val + a_val * percent / 100
                    elif op == "-":
                        result = a_val - a_val * percent / 100
                    elif op == "*":
                        result = a_val * (percent / 100)
                    elif op == "/":
                        result = a_val / (percent / 100)
                    add(f"{expr} = {result}")
                    return result
