import csv

with open('winequality-red1.csv',mode='r') as opened_file_ref:
    csvfile=csv.reader(opened_file_ref)
    print(csvfile)

    for data in csvfile:
        if data[10] > '8': #and data[1] == '2022':
            print(data[1])