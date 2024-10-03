n,number,sum =int(input("inter a number")) , 1 ,0
while number <= n:
    if number % 2 == 0:
        sum += number
        print(sum)
    number += 1
print(f"The sum of even numbers between 1 and {n} is {sum}.")
