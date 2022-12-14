from graphics.rectangle import*
from graphics.circle import*
from graphics.threedgraphics.cuboid import*
from graphics.threedgraphics.sphere import*

l=int(input("enter the length of rectangle :"))
b=int(input("enter the breadth of rectangle :"))
print("Area of the rectanlge :",RectArea(l,b))
print("Perimeter of the rectanlge :",RectPerimeter(l,b))

r=int(input("enter the radius of circle :"))
print("Area of the circle :",CirArea(r))
print("Perimeter of the circle :",CirPerimeter(r))

r1=int(input("enter the radius of sphere :"))
print("Area of the sphere :",SphArea(r1))
print("Perimeter of the sphere :",SphPerimeter(r1))

l1=int(input("enter the length of cuboid :"))
b1=int(input("enter the breadth of cuboid :"))
h1=int(input("enter the breadth of cuboid :"))
print("Area of the cuboid :",CubArea(l1,b1,h1))
print("Perimeter of the cuboid :",CubPerimeter(l1,b1,h1))








