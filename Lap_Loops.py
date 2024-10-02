range_number = range(45, 210)
for numbers in range_number:
    if numbers == 100:
        continue
    elif numbers == 205:
        break
    print(numbers)
qust = "what is the product of 7 * 24 ?"
while input(qust) != str(7*24):
    print("Your Answer is wrong try again.")
else:
    print("You answered this Question correctly")