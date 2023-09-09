print("Enter Sides of a Triangle -->")
x = int(input("Enter the First Side of Triangle: "))
y = int(input("Enter the Second Side of Triangle: "))
z = int(input("Enter the Third Side of Triangle: "))

if(x == y == z):
    print("Equilateral Triangle...")

elif(x == y or y == z or z == x):
    print("Isosceles Triangle...")

else:
    print("Scalene Triangle...")

