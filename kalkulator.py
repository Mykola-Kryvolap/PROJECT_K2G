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


        if expr_clean.endswith("%"):
            result = float(expr_clean[:-1]) / 100
            add(f"{expr} = {result}")
            return result

        open_b = expr.count("(")
        close_b = expr.count(")")
        expr += ")" * (open_b - close_b)

        result = eval(expr, {"math": math, "__builtins__": {}})
        add(f"{expr} = {result}")
        return result

    except ZeroDivisionError:
        raise ZeroDivisionError("Dzielenie przez zero!")
    except Exception:
        raise ValueError("Nieprawidlowe wyrazenie"



