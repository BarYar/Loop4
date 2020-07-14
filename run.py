from B12p3 import *
C=Circle(3,4,5)
Cy=Cylinder(3,4,5,6)
P=Point(8,9)
l=[C,Cy,P]
for i in range(0,len(l)):
    print (l[i].__str__())
