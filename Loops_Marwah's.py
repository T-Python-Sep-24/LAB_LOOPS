#1) Using range(), make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. Skip the number 100 and break the loop at 205

for number in range(45, 211):  
    if number == 100:
        continue  
    if number > 205:
        break  
    print(number)



#2) Using a while loop and input , do the following :

while True:
    answer = input("What is the product of 7 * 24? ")
    
    if answer.isdigit() and int(answer) == 168:  # 7 * 24 = 168
        print("You answered this Question correctly")
        break  # Exit the loop
    else:
        print("Your Answer is wrong, try again..")