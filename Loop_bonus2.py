# Prompt the user for a positive integer
n = int(input("Enter a positive integer: "))

# Initialize the sum to 0
sum_of_evens = 0

# Iterate over the numbers from 1 to n
for i in range(1, n + 1):
    if i % 2 == 0:  # Check if the number is even
        sum_of_evens += i  # Add the even number to the sum

# Print the result
print(f"The sum of even numbers between 1 and {n} is {sum_of_evens}.")