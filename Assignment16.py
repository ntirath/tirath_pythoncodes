# Assignment 16 :  Generate Fibonacci sequence : Author Tirath

a = int(input("Enter the value of which fibonnaci series to be generated, a = "))
b =[1,1]
for i in range(0,a-2):
    c = b[i] + b[i+1]
    b.append(c)
print(b)

d = int(input("Enter the value of which fibonnaci series to be generated, a = "))
e =[]
for i in range(0,d):
    if (i == 0):
        c = 1
        e.append(c)
    elif (i == 1):
        c = 1
        e.append(c)
    elif (i >= 2):
        c = e[i-2] + e[i-1]
        e.append(c)
print(e)