
for number in range(45, 211):
    if number == 100:
        continue
    if number == 205:
        break
    print(number)


Ask = "what is the product of 7 * 24 ? "
product = 7 * 24

while float(input(Ask)) != product:
    print("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly")

    
