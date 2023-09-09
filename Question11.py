def count(str, num):
    i = 0
    j = 0
    while i < len(str):
      if str[i] == num:
         j = j + 1

      i = i + 1
    
    return j


str = input("Enter Integer Number: ")
num = input("Enter a Number: ")
print("Occurrence Count: ", count(str, num))
