''' 
Make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. 
Skip the number 100 and break the loop at 205
'''
for number in range(45, 211):
    if number == 100:
        continue
    if number == 205:
        break
    print(number)

''' 
Ask the the user : "what is the product of 7 * 24 ?"
'''
answer: float = 0
while answer != 168:
    answer = input("what is the product of 7 * 24 ? ")

    if float(answer) == 168:
        print("You answered this Question correctly")
        break
    else:
        print("Your Answer is wrong try again..")