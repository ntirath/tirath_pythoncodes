#Q1 : Power of the list using recursion

def pow_num(n,p):
    if p == 0:
        return 1
    else:
        return (n*(pow_num(n,p-1)))

#n = int(input("Enter the value of the number , n = "))
#p = int(input("Enter the value of the power , p = "))   
n = [0, 1, 2, 4, 10, 23, 30, 43, 52, 67, 78, 100]
res =[]
p = 2
m = len(n)
for i in range(m):
    result= pow_num(n[i],p)
    res.append(result)
#result = pow_num(n,p)
print("The value of the number", n)
print("The value of the power", p)
print("Power of the list = ", res)