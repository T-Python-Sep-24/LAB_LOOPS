#Prompt the user for a positive number 
n: int = int(input("Enter a positive integer: "))

#Range of numbers between 1 and the number in user input
numbers = range(1, n + 1)

#Variable to store the sum
sum: int = 0

#Iterate over the range and calculate sum of even numbers
for num in numbers:
    if num % 2 == 0:
        sum += num
        
#Print results
print(f"Sum of even numbers between 1 and {n} is: {sum}")
