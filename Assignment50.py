# Assignment 50 :  Average numbers in a array : Author Tirath
list1 = [10, 21, 4, 45, 66, 93]

a = len(list1) 
sum_list =0
for i in range(a):
    sum_list = sum_list + list1[i]
avg_list = sum_list / a
print("Average of the all the numbers given in the list ", avg_list)
