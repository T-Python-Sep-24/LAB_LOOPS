n = int(input("Enter a positive integer"))
i = 0
for number in range (1,n):
    if number % 2 == 0 :
        i += number
print("The sum of all even numbers between 1 and", n, "is:", i)