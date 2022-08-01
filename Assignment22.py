# Assignment 22 :  Addition of two matrices : Author Tirath


A = [[1,2,3], 
     [4,5,6],
     [7,8,9]]

B = [[10,20,30],
     [40,50,60],
     [70,80,90]]

# C is the resultant matrix
C = [[0,0,0],
     [0,0,0],
     [0,0,0]]


# iterate through rows it is 3 x 3 matrix
for i in range(3):
   # iterate through columns
   for j in range(3):
       C[i][j] = A[i][j] + B[i][j]

for r in C:
   print(r)