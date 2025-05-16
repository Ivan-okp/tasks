tsk_qnt = int(input("Enter the quantity of your tasks: "))

tasks = []
i = 0

while i <= tsk_qnt - 1:
    tsk = input("Enter your task: ")
    tasks.append(tsk)
    i += 1

processing = input("What do you want to do with your tasks? (delete / add / print all tasks / execute) ")

if processing == "delete":
    dt = input("What task do you want to delete? ")
    tasks.remove(dt)
elif processing == "add":
    at = input("What task do you want to add? ")
    tasks.append(at)
elif processing == "print all tasks":
    print(tasks)
elif processing == "execute":
    print("all your tasks ware executed")
    