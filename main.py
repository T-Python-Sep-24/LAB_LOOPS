
numbers =range(45,210)

for i in numbers:
    if i == 100:
        continue
    if i == 205:
        break
    print(i)

question= input("what is the product of 7 * 24 ?")
while question != "168":
    question= input(" Your Answer is wrong try again..\nwhat is the product of 7 * 24 ?")
else:
    print("You answered this Question correctly")