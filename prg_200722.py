# calculate a^2 + b^2 + 2ab
a = int(input("Enter value of a = "))
b = int(input("Enter value of b = "))

c1 = a**2
c2 = b**2
c3 = 2*a*b

d1 = (a+b)**2
print("The answer for (a+b)**2" =, d1)
d2 = (a**2) + (2*a*b) + (b**2)
print("The answer for (a**2) + (2*a*b) + (b**c)" =, d2)
d3 = c1 + c3 + c2
print("The answer for a^2 + b^2 + 2ab using separately calculated values" =, d3)
