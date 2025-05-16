import random

from random import randint, choice

# first app

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
           "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]

ps = int(input("You have to enter the lenght, to create your new password: ")) - 2
lst = [str(randint(0, 10)) for i in range(ps)]
ps_2 = ""
ps_3 = "".join(lst)
let = random.choice(letters).upper()
let_2 = random.choice(letters)
ps_4 = let + ps_3 + let_2

print(ps_4)

# second app

if ps_4 == input("Enter your password to use analisator: "):
    print("Success")
else:
    print("Try again")

line = input("Enter your text: ")
wrd = input("Enter your word: ")
lenght = input("lenght(yes/no): ")

wrd_2 = "Yes" if wrd in line else "No"
lenght_2 = len(line) if lenght == "yes" else None

print(f"availability of word: {wrd_2}, lenght of line: {lenght_2}")

# third app

if ps_4 == input("Enter your password to use calculator: "):
    print("Success")
else:
    print("Try again")
    
calculator = input("Chose the operation(+, -, /, *, //, %, **): ")
a, b = map(int , input("Enter your figures: ").split())
mx = input("Do you want to know what figure is max(yes/no): ")
if calculator == "+":
    print("Result: ", a + b, sep="")
elif calculator == "-":
    print("Result: ", a - b, sep="")
elif calculator == "*":
    print("Result: ", a * b, sep="")
elif calculator == "/":
    print("Result: ", a / b, sep="")
elif calculator == "//":
    print("Result: ", a // b, sep="")
elif calculator == "%":
    print("Result: ", a % b, sep="")
elif calculator == "**":
    print("Result: ", a ** b, sep="")

if mx == "yes":
    print(max(a, b))
else:
    None