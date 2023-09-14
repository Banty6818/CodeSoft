n1 = int(input("Enter 1st number : "))
n2 = int(input("Enter 2nd number : "))

def add():
    addition = n1 + n2
    print("Addition of ", n1, " and ", n2, " is ", addition)

def sub():
    subtraction = n1 - n2
    print("Subtraction of ", n1, " and ", n2, " is ", subtraction)

def mul():
    multiplication = n1 * n2
    print("Multiplication of ", n1, " and ", n2, " is ", multiplication)

def div():
    division = n1 / n2
    print("Division of ", n1, " and ", n2, " is ", division)

print('''****** Menu ******
1. addition
2. subtraction
3. multiplication
4. division''')

flag = 1
while flag == 1:
    ch = int(input("Enter your choice : "))
    if ch == 1:
        add()
    elif ch == 2:
        sub()
    elif ch == 3:
        mul()
    elif ch == 4:
        div()
    else:
        print("Invalid Choice")

    new_flag = int(input("Enter 1 for continue or 0 for termination : "))
    flag = new_flag

    if flag == 0:
        break