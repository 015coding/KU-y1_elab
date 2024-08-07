import math

def sphere_volume(r):
    return (4/3)*math.pi*r**3

def sphere_surface_area(r):
    return 4*math.pi*r**2

r = float(input("Enter sphere radius: "))
print("Sphere volume is %.2f"% sphere_volume(r))
print("Sphere surface is %.2f" % sphere_surface_area(r))