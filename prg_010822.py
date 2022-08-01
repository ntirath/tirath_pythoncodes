# #identity operator
# a =10
# b = 20
# c = a
# print(a is not b)
# print(a is c)
# #id
# print(id(a))
# print(id(b))

# #Membership operator
# x = 24
# y = 20
# list1 = [10,20,30,40,50]
# if (x not in list1):
#     print(x, "x is Not present in the list")
# else:
#     print(x, "x is present in the list")

# if (y in list1):
#     print(y, "y is present in the list")
# else:
#     print(y, "y is not present in the list")

# list = [1,2,3,4,5]
# for i in range(len(list)):
#     print(list[i], end = " ")

for var in "Python world":
    if var == ' ':
        continue
    print(var, end = " ")