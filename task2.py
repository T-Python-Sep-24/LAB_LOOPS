while True:
    try:
        # Prompt for user input and convert to an integer
        answer = int(input("What is the product of 7 * 24? "))

        # Check if the answer is correct
        if answer == (7 * 24):
            print("You answered this question correctly!")
            break  # Exit the loop if the answer is correct
        else:
            print("Your answer is wrong, try again..")
    
    except ValueError:
        print("That's not a valid integer. Please enter a positive integer.")
