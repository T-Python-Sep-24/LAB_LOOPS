# Define the correct answer
correct_answer = 7 * 24

while True:
#Ask the the user : "what is the product of 7 * 24 ?"
    user_answer = int(input("What is the product of 7 * 24? "))
    
    # Check if the answer is correct
    if user_answer == correct_answer:
        print("You answered this Question correctly!")
        break  # Exit the loop if the answer is correct
    else:
        print("Your answer is wrong, try again...")