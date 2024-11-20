version = "1.0.0"
print(f"you are currently using version {version}.\n")
print("project made by selleck.")
print("-"*38)

import random

userInput1 = input("type START to PUSH YOUR LUCK")
startNumber = random.randint(1, 13)
newNumber = random.randint(1, 13)

print(f"the starting number is {startNumber}\n")

userInput2 = input("would you like to go higher or lower? type Q to quit. not cap sensitive btw.").lower()

while True:  
    if userInput2 == "q":  
        break
    
    if userInput2 == "higher":
        print(" ")
        print(f"the new number is {newNumber}.")
        if newNumber > startNumber: 
            print(f"you win. {newNumber} is higher than {startNumber}")
            break
        else:  
            print(f"you busted. {newNumber} is lower than {startNumber}")
            break
    elif userInput2 == "lower": 
        print(f"the new number is {newNumber}.")
        if newNumber < startNumber: 
            print(f"you win. {newNumber} is lower than {startNumber}")
            break
        else:  
            print(f"you busted. {newNumber} is higher than {startNumber}")
            break