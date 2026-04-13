import math
from historia import add

def calculate(expr):
    try:
        expr = expr.replace("^", "**")
        expr_clean = expr.replace(" ", "")
