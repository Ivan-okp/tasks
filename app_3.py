import random

# first app

fig = random.randint(1, 101)

for i in range(6):

    fig_2 = int(input("Enter your figure: "))

    if fig == fig_2:
        print("Congratuiation, you guesed it !!!")
        break
    else:
        print("Try again")

# second app

dij = int(input("Enter your figure: "))

for i in range(1, int(dij / 2) + 1):
    if dij % i == 0:
        print(i)
