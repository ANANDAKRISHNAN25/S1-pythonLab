'''num = 7
factorial = 1
if num < 0:
    print("factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
print("The factorial of",num,"is",factorial)'''

def calc_factorial(x):
    if x==1:
        return 1
    else:
        return (x*calc_factorial(x-1))

num = int(input("Enter a No: "))
print("The factorial of",num,"is",calc_factorial(num))