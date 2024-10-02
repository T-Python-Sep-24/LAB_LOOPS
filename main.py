for numbers in range (45, 210):
    if numbers == 100: 
        continue    
    elif numbers == 205:
        break
    print(numbers)


test = "What is the product of 7 * 24? "
while int(input(test)) !=  7*24:
    print("Your answer is wrong, try again...")
else:
    print("You answered this question correctly!")

