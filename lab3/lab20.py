def compute_rectangle_area(x,y):
    return x*y

def compute_surface_area(x,y,z):
    return (x*y*2)+(y*z*2) + (z*x*2)

def compute_volume(x,y,z):
    return x*y*z

x = float(input("Enter width: "))
y = float(input("Enter lenght: "))
z = float(input("Enter height: "))
print(f"For [{x:.2f} x {y:.2f} x {z:.2f}] cuboid:")
print("Surface area = %.3f" % compute_surface_area(x,y,z))
print("Volume = %.3f" % compute_volume(x, y ,z))
print()
print("After doubling each side,")
print(f"For [{x*2:.2f} x {y*2:.2f} x {z*2:.2f}] cuboid:")
print("Surface area = %.3f" % compute_surface_area(x*2,y*2,z*2))
print("Volume = %.3f" % compute_volume(x*2,y*2,z*2))
