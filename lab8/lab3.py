import math
class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def get_radius(self):
        return self.radius

    def get_height(self):
        return self.height

    def set_radius(self, new_radius):
        self.radius = new_radius

    def set_height(self, new_height):
        self.height = new_height

    def get_base_area(self):
        return round((math.pi*self.radius**2), 3)

    def get_volume(self):
        return round(math.pi * self.radius ** 2 * self.height, 3)

    def __str__(self):
        return f"Radius: {self.radius:.3f}, Height: {self.height:.3f}"

x = Cylinder(4.123, 2.000)
print(x.get_radius())
print(x.get_height())
x.set_radius(7.000)
x.set_height(14.000)
print(x.get_volume())
print(x.get_base_area())
print(x)