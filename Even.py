print('Enter a positive integer limit number: ')
Limit_number = int(input())
sum = 0
for i in range(Limit_number+1):
    if (i % 2) == 0:
        print(i)
        sum += i
        
print('')
print(f'The sum of even numbers between 1 and {Limit_number} is {sum}.')