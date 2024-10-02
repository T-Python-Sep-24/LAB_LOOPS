'''
## Bonus
'''

positive_int=int(input("Enter a positive number: "))
sumOfEvenNumbers=0
for i in range(1,positive_int+1):
    if i%2 ==0:
        sumOfEvenNumbers+=i
        print(i)

print(f"the sum of even numbers between 1 and {positive_int} is: {sumOfEvenNumbers}")
