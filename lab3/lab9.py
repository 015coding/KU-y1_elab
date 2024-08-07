import math

def area_of_circle(k):
    k = int(k)
    return math.pi *((k/2) ** 2)

d = input("Diameter: ")
d_float = area_of_circle(d)
print('area = %.3f'%(area_of_circle(d)))