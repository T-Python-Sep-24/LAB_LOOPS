i=[]
for i in range (45,211):
    if i == 100:
        continue
    elif i==205:
        break
    print(i)


print("-"*20)


q1=int(input("what is the product of 7 * 24 ?"))
while q1 == 168:
    print("You answered this Question correctly")
    break
else:
    print("Your Answer is wrong try again..")