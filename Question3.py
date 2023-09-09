c = int(input("Enter the Side of Cube: "))
vol1 = (c * c * c)
print("Volume of Cube is: ",vol1)

r = int(input("Enter the Radius of Cylinder: "))
h = int(input("Enter the Height of Cylinder: "))
vol2 = 3.14 * r * r * h
print("Volume of Cylinder is: ",vol2)


x = int(input("Enter the Radius of Cone: "))
y = int(input("Enter the Height of Cone: "))
vol3 = y/3 * (3.14 * x * x)
print("Volume of Cone is: ",vol3)

s = int(input("Enter the Radius of Sphere: "))
vol4 = 4/3 * (3.14 * s * s * s)
print("Volume of Sphere is: ",vol4)