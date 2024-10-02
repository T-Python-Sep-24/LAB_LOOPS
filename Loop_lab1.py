# Define the range from 45 to 210
for num in range(45, 211):  
    if num == 100:
        continue  # Skip number 100
    elif num == 205:
        break  # Break the loop when number 205 is reached
    print(num)