answer = input("Enter a positive integer: ")  
while True:

    
    try:
        n = int(answer)  
        
        if n < 1:  
            print("Please enter a positive integer.")
            continue
        
        sum = 0  
        for number in range(1, n + 1):
            if number % 2 == 0:  
                sum += number  
        
        print(f"The sum of even numbers between 1 and {n} is {sum}.")
        break 
    except ValueError:
        print("That's not a valid integer. Please enter a positive integer.")