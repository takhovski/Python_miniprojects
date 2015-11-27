### Mini Project 1, Ask if the user wants to role a dice and continue

import random #Import the Random library
### Define a function that produces an integer between 1 to 6
def role_dice():  
    x = random.randint(1,6)
    print(x)
###
cond = "TRUE" # Condition for the while loop
while cond == "TRUE":
    role = str(input('Do you wanna role die? (To Role type yes)')) 
    role = role.upper()
    if role == 'YES':
        role_dice()
    else:
        cond == "FALSE"
        break





