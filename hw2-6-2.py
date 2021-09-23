# author: DMH 9/23/21

radius = input("What is the radius")
height = input("What is the height")



surface_area = (2 * (3.14 * int(radius) * int(height))) + (2 * (3.14 * (int(radius) ** 2)))
volume = 3.14 * (int(radius) ** 2) * int(height)

print(surface_area)
print(volume)