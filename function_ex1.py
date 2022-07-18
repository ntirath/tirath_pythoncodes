#example of function
def sqr(num):
    result = num * num
    print("Result of num * num = ", result)
    print("Result of", num, "*", num, "= ", result)

def mul(num1, num2):
    result1 = num1 * num2
    print("Result of num1 * num2 = ", result1)

def div(num3, num4):
    result2 = num3 / num4
    print("Result of num3 / num4 = ", result2)

n = int(input("Enter the value of which square to be calculated = "))
n1 = int(input("Enter the first value to be multiplied ="))
n2 = int(input("Enter the second value to be multiplied = "))
n3 = float(input("Enter the first value to be divided ="))
n4 = float(input("Enter the second value to be divided = "))
sqr(n)
mul(n1,n2)
div(n3,n4)