## 1) Using range(),  make a range from 45 to 210, 
# using a for loop iterate over the sequence and print the elements.
#  Skip the number 100 and break the loop at 205

for n in range(45,210):
    if n ==100:
        n += 1
    elif n == 206:
        break
    else:
        print(n)

## 2) Using a while loop and input , do the following :
while(True):
    product = int(input("what is the product of 7 * 24 ? "))
    if product == 168:
         print("You answered this Question correctly")
         break
    else:
        print("Your Answer is wrong try again..")

    
