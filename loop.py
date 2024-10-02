print("Task 1: Print numbers from 45 to 210, skipping 100 and breaking at 205")
for number in range(45, 211):
    if number == 100:
        continue
    if number > 205:
        break
    print(number)

print("")

print("Task 2: Answer the multiplication question")
while True:
    answer = input("What is the product of 7 * 24? ")
    if answer.isdigit() and int(answer) == 168:
        print("You answered this question correctly.")
        break
    else:
        print("Your answer is wrong, try again..")

print("")

print("Bonus Task: Sum of Even Numbers")
n = int(input("Enter a positive integer: "))

sum_of_evens = 0

for number in range(1, n + 1):
    if number % 2 == 0:
        sum_of_evens += number

print(f"The sum of even numbers between 1 and {n} is {sum_of_evens}.")
