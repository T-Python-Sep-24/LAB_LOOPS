# Creating a range of numbers 
numbers = range(45, 211)

print("Counting..")

# Iterate over the range and print 
for n in numbers:
    if n == 100:
        continue
    elif n == 205:
        break
    else:
        print(n)

# Ask question and take answer as input from user
# Keep reapeating until correct answer is provided
usrAnswer: int = 0
correctAnswer: int = 7 * 24

while usrAnswer != correctAnswer:
    usrAnswer = int(input("What is the product of 7 * 24? "))
    if usrAnswer == correctAnswer:
        print("You answered this question correctly.")
        break
    else:
        print("Your answer is wrong, try again.")
    