# Assignment 23 :  Transpose of matrix : Author Tirath


A = [[1,2,3], 
     [4,5,6]]



# C is the resultant matrix
C = [[0,0],
     [0,0],
     [0,0]]


# iterate through rows it is 2 x 3 matrix
for i in range(3):
   # iterate through columns
   for j in range(2):
       C[i][j] = A[j][i]

for r in C:
   print(r)