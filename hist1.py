import pandas as pd
import matplotlib.pyplot as plt

data  = [['E001', 'M', 34, 123,'NORMAL',350],
         ['E002', 'F', 28, 135,'NORMAL',350],
         ['E003', 'M', 43, 150,'NORMAL',350],
         ['E004', 'F', 50, 156,'NORMAL',350],
         ['E005', 'M', 21, 156,'NORMAL',350],
         ['E006', 'F', 32, 113,'NORMAL',350],
         ['E007', 'F', 22, 163,'NORMAL',350],
         ['E008', 'M', 21, 129,'NORMAL',350],
         ['E009', 'M', 23, 120,'NORMAL',350],
         ['E0010', 'M', 34, 103,'NORMAL',350]]
         
df = pd.DataFrame(data,columns = ['EMPID','Gender','Age', 'Sales', 'BMI','Income'])
df.hist()
plt.show()