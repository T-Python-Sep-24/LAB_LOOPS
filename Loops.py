print('The for-loop prints: ')
for i in range(45, 210):
    if i == 100:
        continue
    if i == 205:
        break
    print(i)
    
print('-' * 15)
print('The while-loop prints: ')
print('')

qusetion = "what is the product of 7 * 24 ?"
while int(input(qusetion)) != 168:
    print('Your Answer is wrong try again..')
else:
    print('You answered this Question correctly')