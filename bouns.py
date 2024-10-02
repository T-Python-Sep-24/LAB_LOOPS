while True:
    
    
    try:
        answer = int(input("Enter a positive integer: "))
        
        sum = 0  
        for number in range(1, answer + 1):
            if number % 2 == 0:  
                sum += number  
        
        print(f"The sum of even numbers between 1 and {answer} is {sum}.")
        break 
    except ValueError:
        print("That's not a valid integer. Please enter a positive integer.")