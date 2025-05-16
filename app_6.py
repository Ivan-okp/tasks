def calculator(a, z, b):
    if z == "+":
        return a + b
    elif z == "-":
        return a - b
    elif z == "/":
        return a / b
    elif z == "*":
        return a * b
    elif z == "//":
        return a // b
    elif z == "%":
        return a % b

opn = input("What do you want to do with your figures('+', '-', '/', '*', '//', '%'): ")
a, b = map(int, input("Enter your figures: ").split())

cl = calculator(a, opn, b)

print(cl)