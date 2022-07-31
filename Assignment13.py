# Assignment 13 :  Check Prime number : Author Tirath

a = int(input("Enter a number to be verified for being prime number: "))


if a > 1:
   for i in range(2,a):
       if (a % i) == 0:
           print("The number entered a = ", a, "is not a prime number")
           break
       else:
            print("The number entered a = ", a, "is a prime number")
       
else:
   print("The number entered a = ", a,"is less then or equal to 1, hence not a prime number")