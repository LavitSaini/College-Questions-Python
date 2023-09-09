import cmath

a = int(input("Enter the Value of a: "))
b = int(input("Enter the Value of b: "))
c = int(input("Enter the Value of c: "))

d = (b * b) - (4 * a * c)
r1 = (-b - (cmath.sqrt(d))) / (2 * a)
r2 = (-b + (cmath.sqrt(d))) / (2 * a)

print("The Root of Quadratic Equation is: ", r1, r2)