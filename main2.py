answer = 168

while True:
    Q1 = input("What is the product of 7 * 24?")
    try:
        Q1 = int(Q1)
        if Q1 == answer:
            print("You answered this question correctly.")
            break
        else:
            print("Your answer is wrong. Try again...")  # Prompt to try again
    except ValueError:
        print("Please enter a valid number.")


