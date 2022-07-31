# Assignment 3 :  Area of Triangle : Author Tirath
print("Area of Equilateral Triangle")
a = int(input("Enter the value of each side of equilateral triangle, a = "))
c =  (3/4)*(a**2)
print("Area of equilateral triangle of each side a = ",a, ";  = ",c)

print("Area of  Triangle using Heron's formula")
a = int(input("Enter the value of each side1 of triangle, a = "))
b = int(input("Enter the value of each side1 of triangle, b = "))
c = int(input("Enter the value of each side1 of triangle, c = "))

d =  (a + b + c)/2
print(d)
e = (d*(d-a)*(d-b)*(d-c)) ** 0.5
print("Area of triangle  = ",e)