import math
while True:
    print("MENU")
    print("1 for addition :")
    print("2 for subtraction :")
    print('3 for multiplication :')
    print("4 for raise to power:")
    print("5 for Division:")
    print("6 for floor division:")
    print("7 for factorial:")
    choice=int(input("enter any choice:"))
    def additon():
        a=int(input("enter 1st no to perform addition:"))         #a-first input
        b=int(input("enter 2nd no to perform addition:"))          #b-second input
        c=a+b
        print("sum is:",c)
        return
    def subtract():
        a = int(input("enter 1st no to perform subtraction:"))
        b = int(input("enter 2nd no to perform subtraction:"))
        c = a - b
        print("subtraction is:", c)
        return
    def multiplication():
        a = int(input("enter 1st no to perform multipication:"))
        b = int(input("enter 2nd no to perform multiplication:"))
        c = a*b
        print("multiplication is:", c)
        return
    def power():
        a = int(input("enter base :"))
        b = int(input("enter power :"))
        c = a**b
        print("division is:", c)
        return

    def divide():
        a = int(input("enter 1st no to perform division:"))
        b = int(input("enter 2nd no to perform division:"))
        c = a/b
        print("division is:", c)
        return
    def floor_division():
        
        
    def factorial():
        num = int(input("enter a number: "))
        if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
        elif num == 0:
        print("The factorial of 0 is 1")
        else:
        for i in range(1,num + 1):
        factorial = factorial*i
        print("The factorial of",num,"is:",factorial)
        return

    if choice==1:
        additon()
    elif choice==2:
        subtract()
    elif choice==3:
        multiplication()
    elif choice==4:
        power()
    elif choice==5:
        divide()
    elif choice==6:
        floor_division()
    elif choice==7:
        factorial()
    else:
        print("wrong input")
        exit(0)
