# Assignment 15 :  Calculate factorial of given number : Author Tirath

a = int(input("Enter the value of which factorial is to be calculated a = "))
b = a + 1
c = 1
for i in range(1,b):
    c = c * i 
    if i == a:
        break
print(c)



