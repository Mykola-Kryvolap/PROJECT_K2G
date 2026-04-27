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
        elif expr == "help":
            print("Operacje: + - * / ^ math.sqrt() %")
            print("Komendy: history | clear | help | exit")
        elif expr == "history":
            hist = get()
            if not hist:
                print("Brak historii")

            else:
                for i, item in enumerate(hist, 1):
                    print(f"{i}. {item}")
        elif expr == "clear":
            clear()
            print("Historia wyczyszczona")
        else:
            try:
                print(calculate(expr))
            except Exception as e:
                print(f"Blad: {e}")

if __name__ == "__main__":
    main()

            


