_history = []
MAX = 100
def add(entry):
    _history.append(entry)
    if len(_history) > MAX:
        _history.pop(0)
def get():
    return list(_history)
