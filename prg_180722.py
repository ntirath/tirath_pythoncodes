#How to get the data type
a = 5
print("Type of a: ", type(a))
b = 5.0
print("Type of b: ", type(b))
c = True
print("Type of c:", type(c))
d = False
print("Type of d:", type(d))
e = "false"
print("Type of e:", type(e))
f = []
print("Type of f:", type(f))

#addition of string or concenetation
string1 = "Tirath"
string2 = "prasad"
string3 = string1 + string2
print("Resultant string3 = ", string3)

#single dimension list
list1 = ['tirath','prasad',34,100.345]
print("First element of list1:", list1[0])
print("Third element of list1:", list1[3])

#Multidimensional list
list2 = ['nagvekar',list1,'Rohit']
print("List 2 = ", list2)
print("Third component of List1 embedded in List2 :", list2[2][3]) # wrong answer
print("Third component of List1 embedded in List2 :", list2[1][3]) # correct answer

list3 = [0,0,0]
list3[0] = "Tirath"
list3[1] = "Prasad"
list3[2] = "Nagvekar"

print("List3 = ", list3)

#Tuple
Tuple1 = (1,2,3)
Tuple2 = (0.1,0.2,0.3)
Tuple3 = Tuple1 + Tuple2
print("Tuple 1 = ", Tuple1)
print("resultant tuple is concetenated tuple:", Tuple3)
Tuple4 = (Tuple1, Tuple2)
print("resultant tuple is the nested tuple:", Tuple4)
print("3rd element of tuple2 in typle4 :", Tuple4[1][2])
Tuple5 = Tuple3 + Tuple4
print("Resultant Tuple5:", Tuple5)
'''
tuple6 =(0,0,0)
tuple6[0] = "Tirath"
tuple6[1] = "Prasad"
tuple6[2] = "Nagvekar"

print("tuple6 = ", tuple6)
Not possible for tuple
'''
#Set
set1 = set()
print("Initial blank Set:", set1)

set2 = set("Python world")
print("\n Set with the use of String:")
print(set2)

print("\nElement of set:")
for i in set2:
    print(i, end ='t')

set3 = set(Tuple5)
print("\n")

print(set3)

print(Tuple5)

Dict1 = {}
print("\nEmpty Dictionary:")
print(Dict1)

Dict2 = {1: 'Tirath', 2:'Prasad', 3:'Nagvekar'}
print("\nDictionary with the use of Integer keys", Dict2)
print("\nValue associated with key2", Dict2[2])


Dict3 = {"Tirath":'Prasad', 1:[1,2,3,4]}
print("\nDictionary with the use of Mixed keys: ", Dict3)
print("\nValue associated with Tirath", Dict3["Tirath"])
print("\nValue associated with Tirath", Dict3[1][1])