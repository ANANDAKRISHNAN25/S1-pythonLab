n=int(input("Enter the number : "))
factors = [i for i in range(1,n+1) if n % i==0]
print("The factors of the number are :",factors)