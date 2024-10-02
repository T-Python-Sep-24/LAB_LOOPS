
num = int(input("Enter a number: "))
sumEven = 0
for i in range(1, num + 1):
    if (i % 2) == 0:
        sumEven = sumEven + i
        print("i = ", i)
    else:
        continue
print("The sum of even numbers between 1 and", num, "is", sumEven)