from kalkulator import calculate
from historia import get , clear

def main():
    print("=" * 40)
    print("  Kalkulator CLI v1.0")
    print("=" * 40)
    print("Komendy: history | clear | help | exit")
    while True:
        expr = input(">>> ").strip()
        if expr == "":
            continue
        elif expr == "exit":
            print("Do widzenia!")
            break


