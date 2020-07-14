import math
class Shape:
    def __init__(self):
        self.area=0
        self.volume=0
    def getArea(self):
        return self.area
    def getVolume(self):
        return self.volume
    def setArea(self,num):
        self.area=num
    def setVolume(self, num):
            self.volume = num
class Point(Shape):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        super().__init__()
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self,num):
        self.x=num
    def setY(self, num):
            self.x = num
    def __str__(self):
        return ("Object type",type(self),",area:",self.getArea(),"volume:",self.getVolume(),"x:",self.getX(),"y:",self.getY())
class Circle(Point):
    def __init__(self,r,x,y):
        self.r=r
        super().__init__(x,y)
        self.setArea(math.pi*math.pow(self.r, 2))
    def getR(self):
        return self.r
    def setR(self,num):
        self.r=num
    def circumference(self):
        return 2*math.pi*self.r
    def __str__(self):
        return ("Object type", type(self), ",area:", self.getArea(), "volume:", self.getVolume(), "r:", self.getR())
class Cylinder(Circle):
    def __init__(self,h,r,x,y):
        self.h=h
        super().__init__(r,x,y)
        self.setArea(math.pi*math.pow(self.r, 2)*h)
        self.setVolume((math.pi*math.pow(self.r, 2)*2)+(2*math.pi*self.r*self.h))
    def getH(self):
        return self.h
    def setH(self,num):
        self.h=num
    def __str__(self):
        return ("Object type",type(self),",area:",self.getArea(),"volume:",self.getVolume(), "h:", self.getH())




