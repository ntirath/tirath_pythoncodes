# Assignment 26 :  Create Pyramid Patterns of Numbers Till 10 : Author Tirath

num_rows = int(input("Enter number of rows: "))

for i in range(num_rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")