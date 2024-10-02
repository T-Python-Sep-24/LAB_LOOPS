# Prompt the user for a positive integer
n = int(input("Enter a positive integer: "))

# Initialize the sum variable
sum_of_evens = 0

# Calculate the sum of even numbers between 1 and n
for number in range(1, n + 1):
    if number % 2 == 0:  # Check if the number is even
        sum_of_evens += number

# Print the result
print(f"The sum of even numbers between 1 and {n} is {sum_of_evens}.")