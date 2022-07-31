# Assignment 12 :  Find the Largest Among Three Numbers : Author Tirath

a = int(input("Enter the value of a = "))
b = int(input("Enter the value of b = "))
c = int(input("Enter the value of c = "))


if (a>b):
    if (a>c):
        print("The value entered a =",a,"is greater then b =", b, "and c =",c)

if (b>a):
    if (b>c):
        print("The value entered b =",b,"is greater then a =", a, "and c =",c)

if (c>a):
    if (c>b):
        print("The value entered c =",c,"is greater then a =", a, "and b =",b)
