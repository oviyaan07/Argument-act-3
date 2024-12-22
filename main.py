def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return (x*factorial(x-1))
num=int(input("enter the number of which you want to find the factorial of "))
a=factorial(num)
print (f"the facorial of {num} is {a}")