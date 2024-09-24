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

n = Line(1, 1, 4, 4)

print(f"{n.get_x1()} {n.get_y1()} {n.get_x2()} {n.get_y2()}")
print(n.contains(0.0, 0.0))
print(n.contains(1.0, 1.0))
print(n.contains(1.0, 0.0))
print(n.contains(0.0, 1.0))
print(n.contains(2.0, 0.0))
print(n.contains(0.0, 3.0))
print(n.get_distance())
print(n.get_y(3))
print(n.get_y(0))
