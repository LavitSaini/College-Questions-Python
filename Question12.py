from statistics import geometric_mean, harmonic_mean, mean

n = int(input("Enter Size of Series: "))
arr = []

for i in range(0 , n):
    x  = int(input())
    arr.append(x)

print("Arithmetic Mean of Given Series is: ", mean(arr))

print("Geometric Mean of Given Series is: ", geometric_mean(arr))

print("Harmonic of Given Series is: ", harmonic_mean(arr))
