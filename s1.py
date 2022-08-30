# Assignment 16 :  Generate Fibonacci sequence : Author Tirath
m = int(input("Enter the value of which fibonnaci series to be generated, a = "))
n =[]

#def lambda_z():
#    return lambda f,g : f + g

for i in range(0,m):
    if (i == 0):
        c = 0
        n.append(c)
    elif (i == 1):
        c = 1
        n.append(c)
    elif (i >= 2):
        f = n[i-2]
        g = n[i-1]
        #c = lambda_z()
        res= lambda f,g : f + g
        n.append(res)
print(n)

