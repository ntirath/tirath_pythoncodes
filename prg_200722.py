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
print("Check if a is greater then or equal to b = ", a>=b)
print("Check if a is less then or equal to a = ", a<=b)

#Logical operators
a = True
b = False
print("Logical AND condition = ", (a and b))
print("Logical OR condition = ", (a or b))
print("Logical NOT condition for a = ", (not a))
print("Logical NOT condition for b = ", (not b))

b = 0b0101 # binary representation of 4
a = 0b1010 # binary representation of 10


c = a&b
print("Value of bit wise ANDing = ",c)
c = a|b
c = bin(c)
print("Value of bit wise ORing = ",c)
c = ~a
c = bin(c)
print("Value of bit wise NOT on a = ",c)
c = ~b
c = bin(c)
print("Value of bit wise NOT on b = ",c)
c = a^b
c = bin(c)
print("Value of bit wise XOR = ",c)
c = a>>2
c = bin(c)
print("Shifting 2 spaces to right of a value = ", c)
c = a<<2
c = bin(c)
print("Shifting 2 spaces to left of a value = ", c)