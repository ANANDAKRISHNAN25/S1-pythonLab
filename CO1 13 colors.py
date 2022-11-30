list1=[]
n=int(input("enter the no:of elements :\n"))
for i in range(0,n):
    a=(input())
    list1.append(a)
print(list1,sep=',')
print(list1[0],list1[-1])