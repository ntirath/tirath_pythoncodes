# Assignment 25 :  To find the string is Palindrome or not : Author Tirath

s = input("Enter the string need to be verified for being Palindrome : ")
A = [s]
B =[]
a=len(A[0])
e = A[0]

for i in range(a):
    c = A[0][a-i-1]
    B.append(c)


for i in range(a):
    if (i == 0):
        d = B[i]
    elif (i > 0):
        d = d + B[i]


if (e == d):
    print("The given string is palindrome")
else:
    print("The given string is not palindrome")