n =int(input("Enter a positive integer: ") )
sum = 0
number = 1

while number <= n:
    if number % 2 == 0:
        sum += number
    number += 1
print("The sum of even numbers between 1 and {} is : {}".format(n,sum))