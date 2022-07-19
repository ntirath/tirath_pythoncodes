# Calculate the length of string
a = input("Enter the string = ")
b = len(a)
print("Length of string = ", b)

#Sum of items in a list
L1 = [12.34, 5, 32, 0.123, 67]
S1 = L1[0] + L1[1] + L1[2] + L1[3] + L1[4]
print("Summation of all items in list = ", S1)

#Sum of items in a list using for-loop
L1 = [12.34, 5, 32, 0.123, 67]
sum2 = 0
for i in range(5):
    sum2 = sum2 + L1[i]
print("Summation of all items in list using for loop = ", sum2)
    


#Check given key is in a dictionary for keys are not integers

dict1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60, 'g': 70}
def key_check(x):
  if x in dict1:
      print("Given key", s, " exists in Dictionary Dict1")
  else:
      print("Given key", s," does not exist in Dictionary Dict1")
s = input("Enter the value of key = ")
key_check(s)

#Check given key is in a dictionary for keys are integers

dict1 = {1: 1.0, 2: 2.0, 3: 3.0, 4: 4.0, 5: 5.0, 6: 6.0, 7: 7.0}
def key_check(x):
  if x in dict1:
      print("Given key", s, " exists in Dictionary Dict1")
  else:
      print("Given key", s," does not exist in Dictionary Dict1")
s = int(input("Enter the value of key = "))
key_check(s)

#Change the given string to change first and last characters
L0 = ['Tirath']
print("String input is : ", L0)
c1 = L0[0][0]
c2 = L0[0][1]
c3 = L0[0][2]
c4 = L0[0][3]
c5 = L0[0][4]
c6 = L0[0][5]

L1 = c6+c2+c3+c4+c5+c1
print(L1)

