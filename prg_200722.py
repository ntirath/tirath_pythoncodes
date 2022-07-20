# calculate a^2 + b^2 + 2ab
a = int(input("Enter value of a = "))
b = int(input("Enter value of b = "))

c1 = a**2
c2 = b**2
c3 = 2*a*b

d1 = (a+b)**2
print("The answer for (a+b)**2 = ", d1)
d2 = (a**2) + (2*a*b) + (b**2)
print("The answer for (a**2) + (2*a*b) + (b**c) = ", d2)
d3 = c1 + c3 + c2
print("The answer for a^2 + b^2 + 2ab using separately calculated values = ", d3)

#Comparison operators
a = int(input("Enter the value of a = "))
b = int(input("Enter the value of b = "))
print("Check if a >b =", a>b)
print("Check if a < b =", a<b)
print("Check if a is equal to b =", a==b)
print("Check if a is not equal to a = ", a!=b)
print("Check if a is greater then or equal to b =", a>=b)
print("Check if a is less then or equal to a = ", a<=b)

#Logical operators
a = True
b = False
print("Logical AND condition = ", (a and b))
print("Logical OR condition = ", (a or b))
print("Logical NOT condition for a = ", (not a))
print("Logical NOT condition for b = ", (not b))
