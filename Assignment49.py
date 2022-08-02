# Assignment 49 : Calculate gross salary from basic salary: Author Tirath

Basic_salary = float(input("Enter the value of Basic salary = "))
DA = (10/100)*Basic_salary
HRA = (20/100)*Basic_salary
CA = (2.5/100)*Basic_salary
EA = (2.5/100)*Basic_salary
MI = (2.5/100)*Basic_salary
IT = (10.41667/100)*Basic_salary
PF = (12/100)*Basic_salary

Gross_Salary = Basic_salary + DA + HRA + CA + EA + MI + IT + PF
print("Basic Salary Rs.",Basic_salary,"/-")
print("Dearness Allowance Rs.",DA,"/-")
print("House Rent Allowance Rs.",HRA,"/-")
print("Conveyance Allowance Rs.", CA,"/-")
print("Entertainment Allowance Rs.", EA,"/-")
print("Medical Insurance Rs.",MI,"/-")
print('Income tax Rs.%0.1f' %IT,"/-")
print("Providend Fund Rs.",PF,"/-")
print('Gross Salary Rs.%0.1f' %(Gross_Salary),"/-")