# Assignment 37 :  Reverse the number : Author Tirath

a = int(input("Enter the value to be reversed, a = "))
reversed_a = 0

while a != 0:
    d = a % 10
    reversed_a = reversed_a * 10 + d
    a //= 10

print("Reversed Number: " + str(reversed_a))
