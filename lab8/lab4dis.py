class Line:
    def __init__(self, x1, y1, x2, y2):
        self.start_point = [x1, y1]
        self.end_point = [x2, y2]
        self.slope = (y2 - y1) / (x2 - x1)
        self.intercept = y1 - self.slope * x1

    def contains(self, x, y):
        expected_y = self.slope * x + self.intercept
        if y == expected_y:
            if min(self.start_point[0], self.end_point[0]) <= x <= max(self.start_point[0], self.end_point[0]) and min(self.start_point[1], self.end_point[1]) <= y <= max(self.start_point[1], self.end_point[1]):
                return True
        return False

    def get_distance(self):
        return ((self.start_point[0] - self.end_point[0]) ** 2 + (self.start_point[1] - self.end_point[1]) ** 2) ** 0.5

    def get_x1(self):
        return self.start_point[0]

    def get_y1(self):
        return self.start_point[1]

    def get_x2(self):
        return self.end_point[0]

    def get_y2(self):
        return self.end_point[1]

    def get_y(self, x):
        if x > max(self.start_point[0], self.end_point[0]) or x < min(self.start_point[0], self.end_point[0]):
            return -999.999
        return self.slope * x + self.intercept


x1 = int(input("Enter x1 : "))
y1 = int(input("Enter y1 : "))
x2 = int(input("Enter x2 : "))
y2 = int(input("Enter y2 : "))
l = Line(x1, y1, x2, y2)
print(f"value of x1 on this line is {l.get_x1():.3f}")
print(f"value of x2 on this line is {l.get_x2():.3f}")
print(f"value of y1 on this line is {l.get_y1():.3f}")
print(f"value of y2 on this line is {l.get_y2():.3f}")
print("==========")
print("Check x and y are on this line ?")
x = int(input("Enter x : "))
y = int(input("Enter y : "))
if l.contains(x, y):
    print(f"x = {x:.3f} and y = {y:.3f} are on this line")
else:
    print(f"x = {x:.3f} and y = {y:.3f} are not on this line")
print(f"Distance between startPoint and endPoint is {l.get_distance():.3f}")
print("==========")
print(f"Find value of y that gives( x , y ) on this line")
x_1 = int(input("Enter x : "))
print(f"value of y is {l.get_y(x_1):.3f}")
if l.get_y(x_1) == -999.999:
    print(f"( x , y ) = ( {x_1:.3f} , {l.get_y(x_1):.3f} ) is not on this line")
else:
    print(f"( x , y ) = ( {x_1:.3f} , {l.get_y(x_1):.3f} ) on this line")