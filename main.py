#1
numbers = list(range(45,211)) #range from 45 to 210 
for number in numbers:
    if number == 100: 
        continue 

    elif number == 205:
        break 
    print(number)

#2
correctAnswer = 7 * 24

while True:
     
     question =int(input("what is the product of 7 * 24 ?  "))
     answer = question
     if answer == correctAnswer:
           print("You answered this Question correctly")
           break
     else:
           print("Your Answer is wrong try again.")
           