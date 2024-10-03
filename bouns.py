n = int(input("Enter a positive integer: "))
value = 0

for number in range(1,n+1):

    if number % 2 == 0:
        value += number  

print(f"The sum of even numbers between 1 and {n} is {value}.")