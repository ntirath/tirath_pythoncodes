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
list2 = ['nagvekar',list1,'Rohit']
print("List 2 = ", list2)
print("Third component of List1 embedded in List2 :", list2[2][3]) # wrong answer
print("Third component of List1 embedded in List2 :", list2[1][3]) # correct answer
Tuple1 = (1,2,3)
Tuple2 = (0.1,0.2,0.3)
Tuple3 = Tuple1 + Tuple2
print("Tuple 1 = ", Tuple1)