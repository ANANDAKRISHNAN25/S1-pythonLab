class Rectangle:
    def __init__(self):
        self.__length=int(input("Enter the length:"))
        self.__width=int(input(("Enter the width:")))
    def __lt__(self,obj2):
        area1=self.__length*self.__width
        
        area2=obj2.__length*obj2.__width
        print("Area of the rectangle 1 is",area1)
        print("Area of the rectangle 2 is",area2)
        return area1<area2
print("Enter the length and breadth of First object:")
obj1=Rectangle()
print("Enter the length and breadth of Second object:")
obj2=Rectangle()

if obj1 < obj2:
    print("Rectangle 1 Area is less than Rectangle 2")
else:
    print("Rectangle 1 Area is greater than Rectangle 2")

    