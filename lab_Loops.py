# For loop with range
for i in range(45, 210):

    if i == 100:
        continue
    if i == 205:
        break
    print("i = ", i)

# While loop
while True:
    ans = int(input("What is the product of 7 * 24 ? "))
    if ans == (7 * 24):
        print("You answered this Question correctly")
        break
    else:
        print("Your Answer is wrong try again..")
