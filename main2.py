pos_int = int(input("Enter a positive integer: "))
sum_even = 0
for i in range(1, pos_int + 1):
    if i % 2 == 0:
        sum_even += i
print(f"The sum of even numbers between 1 and {pos_int} is {sum_even}.")