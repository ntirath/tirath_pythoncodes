# Assignment 19 :  Find factors of the number : Author Tirath


a = int(input("Enter the value of which factors are to be determined, a = "))
b=[]
for i in range(1, a+1):
    c = a%i
    if (c == 0):
        b.append(i)
print(b)
    