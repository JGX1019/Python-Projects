import random

Attempts = 0

while True:
    Range = input("Please enter a positive integer: ")

    try:
        Range = int(Range)
        if Range > 0:
            break  
        else:
            print("The number must be positive. Please try again.")
    except ValueError:
        print("That's not an integer. Please try again.")

Random = random.randint(0, Range)

while True:
    Guess = input(f"Guess the random number between 0 and {Range}: ")
    Attempts += 1

    try:
        Guess = int(Guess)
        if Guess < Random:              
            print("Below the number")
        elif Guess > Random:
            print("Above the number")
        elif Guess == Random:
            print("Good job!")
            break
        else:
            print("The number must be positive. Please try again.")
    except ValueError:
            print("That's not an integer. Please try again.")

print(f"You got the correct answer in {Attempts} guess(es)")

        
          
       
         
            
    
        

    
