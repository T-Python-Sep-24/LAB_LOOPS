# For loop with range
for i in range(45,210):

    if i == 100:
        continue
    if i == 205:
        break
    print("i = ", i)

# While loop
while True:
    ans = int(input("What is the product of 7 * 24 ? "))
    if ans == 7 * 24:
        print("correct")
        break
    else:
        print("Wrong, Try again")
