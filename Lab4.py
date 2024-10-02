# Lab 4

#The Answer for number 1
myRange = range(45,210)

for myRangeLoop in myRange:
    if myRangeLoop == 100:
        continue
    elif myRangeLoop == 205:
        break
    print(myRangeLoop)



#The Answer for number 2
print("Welcome to your Math Quiz")

print("-" * 20)

#The Answer

while True:
    userAnswer = int (input ("what is the product of 7 * 24 ?:"))
    if userAnswer == 168:
        print("You answered this Question correctly")
        break
    
    else:
        print("Your Answer is wrong try again..")
    