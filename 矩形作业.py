class NotaRectangle(Exception):
    pass
class NotaSquare(Exception):
    pass

class Rectangle():
    def __init__(self):
        while True:
            try:
                self.x1=float(input("please input x1 "))
                self.x2=float(input("please input x2 "))
                self.y1=float(input("please input y1 "))
                self.y2=float(input("please input y2 "))
                if self.x1-self.x2==0 or self.y1-self.y2==0:
                    raise NotaRectangle()
                else:
                    break
            except(NotaRectangle):
                print("x1不能等于x2，y1不能等于y2")
                    
            
    
                      
    def width(self):
        width=abs(self.x1-self.x2)
        return width
                      
    def height(self):
        height=abs(self.y1-self.y2)
        return height
                      
    def area(self):
        return self.width*self.height
                      
    def circumference(self):
        return 2*(self.width+self.height)

class Square(Rectangle):
    def __init__(self):
        while True:
            try:
                self.x1 = float(input("please input x3 "))
                self.x2 = float(input("please input x4 "))
                self.y1 = float(input("please input y3 "))
                self.y2 = float(input("please input y4 "))
                if self.x1-self.x2 != self.y1-self.y2:
                    raise NotaSquare()
                else:
                    break
            except(NotaSquare):
                print("正方形长宽必须相等")


                      
r1 = Rectangle()
print("矩形的长为 %f"%r1.height())
print("矩形的宽为 %f"%r1.width())
print("矩形的周长为 %f"%r1.circumference())
print("矩形的面积为 %f"%r1.area())
r2=Rectangle()
print("矩形的长为 %f"%r2.height())
print("矩形的宽为 %f"%r2.width())
print("矩形的周长为 %f"%r2.circumference())
print("矩形的面积为 %f"%r2.area())

r3=Square()
print("正方形的长为 %f"%r3.height())
print("正方形的宽为 %f"%r3.width())
print("正方形的周长为 %f"%r3.circumference())
print("正方形的面积为 %f"%r3.area())

r4=Square()
print("正方形的长为 %f"%r4.height())
print("正方形的宽为 %f"%r4.width())
print("正方形的周长为 %f"%r4.circumference())
print("正方形的面积为 %f"%r4.area())
