# 2. Guess the Number
# Computer guesses a number and the user tries to guess it.
import random
# Function that compares two numbers and guides the user towards the right answer.
def compare(x,y): 
    if x > y:
        print ("My number is smaller.")
        cond = True
        return cond
    elif x< y:
        print ("My number is bigger.")
        cond = True
        return cond
    else:
        cond = False
        print ("Great! That's my number")
        return cond
                

print("I am going to guess a number between 1 and 100")
number = random.randint(1,100) # the number that computer imagines.
print("I did!")
condition = True
while condition == True:
    temp = int(input("Guess my number. Good Luck!     "))
    condition = compare(temp,number)
    
