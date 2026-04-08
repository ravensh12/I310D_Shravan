import math

def calculate_volume_of_sphere(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

print("Volume for radius 30:", calculate_volume_of_sphere(30))
print("Volume for radius 40:", calculate_volume_of_sphere(40))