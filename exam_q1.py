#Power of the number using recursion

def pow_num(n,p):
    if p == 0:
        return 1
    else:
        return (n*(pow_num(n,p-1)))

n = int(input("Enter the value of the number , n = "))
p = int(input("Enter the value of the power , p = "))    
result = pow_num(n,p)
print("Power of the number  = ", result)