# Assignment 11 :  Check if number is odd or even : Author Tirath

a = float(input("Enter the value to be verified = "))
b = (a %2)
if (b == 0):
    print("The value entered a =",a,"is even")
else:
    print("The value entered a =",a,"is odd")