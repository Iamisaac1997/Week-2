import math

class Point:                                                                                        #利用物件導向定義點
    def __init__(self, x, y):                                                                       #定義座標(x,y)
        self.x = x  
        self.y = y

class Line:                                                                                         #利用物件導向定義線
    
    def __init__(self, p1, p2):                                                                     #定義線的(x,y)分別的點
        self.p1 = p1
        self.p2 = p2

    def slope(self):                                                                                #計算斜率
        if self.p1.x-self.p2.x == 0:
            return float('inf')
        else:
            return (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)

    def parallel(self, other_line):                                                                 #判斷平行
        if self.slope() == other_line.slope():
          return True
        else:
          return False

    def perpendicular(self, other_line):                                                            #判斷是否會相交
        if self.slope() == float('inf') and other_line.slope() == 0:
            return True
        if self.slope() == 0 and other_line.slope() == float('inf'):
            return True
        if self.slope() == float('inf') or other_line.slope() == float('inf'):
            return False
        if abs(self.slope() * other_line.slope() + 1) < 0 :
            return True
        return False

class Circle:                                                                                       #利用物件導向定義圓
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def area(self):                                                                                 #計算面積
        return math.pi * self.radius**2

    def intersect(self, another_circle):
        distance = math.sqrt((self.center.x - another_circle.center.x)**2 + (self.center.y - another_circle.center.y)**2)
        return distance <= self.radius + another_circle.radius

class Polygon:                                                                                      #利用物件導向定義四邊形
    def __init__(self, points):
        self.points = points

    def perimeter(self):                                                                            #計算各點長度
        perimeter = 0
        for i in range(len(self.points)):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % len(self.points)]
            distance = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
            perimeter += distance
        return perimeter

p_1 = Point(-6, 1)
p_2 = Point(2, 4)
p_3 = Point(-6, -1)
p_4 = Point(2, 2)
p_5 = Point(-1, 6)
p_6 = Point(-4, -4)
p_7 = Point(6, 3)
p_8 = Point(8, 1)
p_9 = Point(2, 0)
p_10 = Point(5, -1)
p_11 = Point(4, -4)
p_12 = Point(-1, -2)

Line_A = Line(p_1, p_2)
Line_B = Line(p_3, p_4)
Line_C = Line(p_5, p_6)

Circle_A = Circle(p_7, 2)
Circle_B = Circle(p_8, 1)

Polygon_A = Polygon([p_9, p_10, p_11, p_12])

print(f"Line A 是否平行於 Line B: {Line_A.parallel(Line_B)}")
print(f"Line C 是否垂直於 Line A: {Line_C.perpendicular(Line_A)}")
print(f"Circle A 的面積: {Circle_A.area()}")
print(f"Circle A 是否與 Circle B 相交: {Circle_A.intersect(Circle_B)}")
print(f"Polygon A 的周長: {Polygon_A.perimeter()}")