#Sorting in Ascending order
a =[1,0,10,30,23,78,100,4,2,43,52,67]
a.sort()
print(a)

a =[1,0,10,30,23,78,100,4,2,43,52,67]
n = len(a)
for i in range(n):
    j = i+1
    for j in range(n):
        if(a[i] < a[j]):
            s = a[i]
            a[i] = a[j]
            a[j] = s
print(a)