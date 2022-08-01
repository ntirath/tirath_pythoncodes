# Assignment 21 :  Make a simple calculator : Author Tirath


a = float(input("Enter the value of a, a = "))
b = float(input("Enter the value of b, b = "))
while(1):

    op = input("Enter the type of operation : +, -, *, /, type exit if want to exit calculator :->  ")

    if (op == '+'):
        c = a + b
        print("Addition of a = ",a,"and b = ", b, " a + b = ", c)
    elif (op == '-'):
        c = a - b
        print("Substraction of a = ",a,"and b = ", b, " a - b = ", c)
    elif (op == '*'):
        c = a * b
        print("Multiplication of a = ",a,"and b = ", b, " a * b = ", c)
    elif (op == '/'):
        c = a / b
        print("Division of a = ",a,"and b = ", b, " a / b = ", c)
    elif (op == 'exit'):
        break