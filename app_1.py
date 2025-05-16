mng = int(input("Enter your mark (100 / 90 / 80 / 70 / 60 / 50): "))

if not mng != 100:
    print("You are in the best group!")
elif mng == 90:
    print("You almost get the best result")
elif mng == 80:
    print("So, it's not so bad")
else:
    if mng == 70:
        print("You result could be better")
    elif mng == 60:
        print("It's almost fail")
    else:
        print("It's faul")

