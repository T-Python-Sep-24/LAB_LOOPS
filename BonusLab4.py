#Bouns for Lab 4
       
#The Answer
n = int(input("Enter a positive integer: "))

even_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:  
        even_sum += i  

print(f"The sum of even numbers between 1 and {n} is {even_sum}.")
