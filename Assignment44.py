# Assignment 44 : Sort Dictionary key and value lists: Author Tirath

dict1 = {'Tirath': [4,3,2,1], 'Prasad': [20,44,99,66], 'Nagvekar': [0.2,-0.4,0,4,1.0,0.05]}

print("The unsorted  dictionary is : " ,dict1)

sorted_dict1 = {}
for i in sorted(dict1):
    sorted_dict1[i] = sorted(dict1[i])

print("The resultant sorted dictionary : " , sorted_dict1) 