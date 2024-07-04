def fibonacci_recursive(a, b, rangee):
    print(a, b, end=" ")  # Print a and b only once
    _fibonacci_recursive(a, b, rangee)

def _fibonacci_recursive(a, b, rangee):
    if rangee >= 3:
        c = a + b
        print(c, end=" ")
        return _fibonacci_recursive(b, c, rangee - 1)

a = 0
b = 1
fibonacci_recursive(a, b, 10)