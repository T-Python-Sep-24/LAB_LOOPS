totalEven = 0 
enterUser = int(input("Enter number:"))
for evenNumbers in range(1,enterUser+1):
    if evenNumbers % 2 == 0:
        totalEven += evenNumbers 
        print(f"These are even numbers:{evenNumbers}")
print(f"This is total : {totalEven}" )