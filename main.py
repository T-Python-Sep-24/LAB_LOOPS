#LAB_LOOPS(1)
for number in range(45,210):
    if number ==100:
        continue
    if number == 205:
        break
    print(number)

#LAB_LOOPS(2)
print("-"*15)
coorect_answer= 7*24
user_answer= None
while user_answer != coorect_answer:
    user_answer= int(input("What is the prodect of 7*24?"))
    if user_answer== coorect_answer:
        print("You answered this Question correctly")
    else:
        print("Your Answer is wrong , try again.")

#Bonus
n=int (input("Enter a positive integer:"))
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum+=i
        print(f"The sum of even numbers between 1 and {n} is {sum}")