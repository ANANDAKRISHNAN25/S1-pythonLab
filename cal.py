import calculator
print("select operation :\n")
print(" 1.Addition\n 2.Substraction\n 3.Multiplication\n 4.Division\n")
choice=input("please enter your choice(1/2/3/4):")
num_1=int(input("enter the first number :"))
num_2=int(input("enter the second number :"))

if choice == '1':
    print(num_1,"+",num_2,"=",calculator.sum(num_1,num_2))
    
elif choice == '2':
    print(num_1,"-",num_2,"=",calculator.sub(num_1,num_2))
    
elif choice == '3':
    print(num_1,"*",num_2,"=",calculator.pro(num_1,num_2))
    
elif choice == '4':
    print(num_1,"/",num_2,"=",calculator.div(num_1,num_2)) 

