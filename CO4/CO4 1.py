class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        
        
    def get_perimeter(self):
        return 2 * (self.length + self.breadth)
    
    def get_area(self):
        return self.length * self.breadth
    
    def compare(self,r2):
        try:
            if self.get_area() == r2.get_area():
              print("Both rectangle have same area")
            
            elif self.get_area() < r2.get_area():
                print("Rectangle r2 is the biggest")
                
            else:
                print("Rectangle r1 is the biggest")
            
        except:
               print("can't be displayed")
l1=int(input("Enter the length of rectangle r1 :"))              
b1=int(input("Enter the breadth of rectangle  r1 :"))
l2=int(input("Enter the length of rectangle r2 :"))              
b2=int(input("Enter the breadth of rectangle  r2 :"))  
r1=rectangle(l1,b1)
r2=rectangle(l2,b2)
print("Area of rectangle r1 : ",(r1.get_area()))
print("Perimeter of rectangle r1 : ",(r1.get_perimeter()))
print("Area of rectangle r2 : ",(r2.get_area()))
print("Perimeter of rectangle r2 : ",(r2.get_perimeter()))
r1.compare(r2)
    
        
