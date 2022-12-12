from math import sqrt
n=int(input("enter a limit :"))
print("The perfect squared Dates between 1000 and",n,"are :")
for i in range(1000,n):
    if sqrt(i)==int(sqrt(i)) and i%2==0:
         print(i)
        