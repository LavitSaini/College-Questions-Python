
def Sum(n):
    i = 1
    sum = 0
    while(i <= n):
       sum += i
       i = i + 1

    print("Sum is: ", sum)

n = int(input("Enter a Number: "))
Sum(n)