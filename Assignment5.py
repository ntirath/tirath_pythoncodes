# Assignment 5 :  Compound Interest : Author Tirath

P = float(input('Enter the value of Principal amount: '))
T = float(input('Enter the value of time frame: '))
R = float(input('Enter rate of interest: '))

CI = P * ( (1+R/100)**T - 1)
print('Compound interest value calculated = %0.4f' % (CI))