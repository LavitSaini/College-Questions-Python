def Table(num):
    i=1
    while(i<=10):
        print(num, "x", i, "=", num * i)
        i = i + 1


num = int(input("Enter a Number: "))
Table(num)