n=int(input("Enter a limit : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        a=i*j
        print(a,end=" ")
    print("\n")