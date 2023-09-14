tasks = []
completed = []

def listing():
    n = int(input("Enter the number of Tasks:"))
    for i in range(n):
        task = input("Enter Task:")
        tasks.append(task)

def updating():
    update = int(input("Enter the number of Tasks for update:"))
    for i in range(update):
        task = input("Enter Task:")
        tasks.append(task)

def track():
    for i in range(len(tasks)):
        inp = int(input("Enter '1' for continue the tasks and '0' for terminate the task:"))

        if inp == 1:
            print("for ", tasks[i], "is completed or not")
            flag = input("Enter the value 'y' if task completed else 'n':")

            if flag == 'y':
                completed.append(tasks[i])

        if inp == 0:
            break

def display():
    print("Total tasks are ", len(tasks))

    for i in range(len(tasks)):
        print("Task", i, ":", tasks[i])

    for j in range(len(completed)):
        print("Completed Task", j, ":", completed[j])

print('''************** Menu ************** 
1. Listing
2. Updating
3. Tracking
4. Display''')

status = 'y'
while status == 'y':
    ch = int(input("Enter your choice:"))
    if ch == 1:
        listing()
    elif ch == 2:
        updating()
    elif ch == 3:
        track()
    elif ch == 4:
        display()
    else:
        print("Invalid Input")

    new_status = input("Enter 'y' for continue and 'n' for terminating:")
    status = new_status

    if status == 'n':
        break