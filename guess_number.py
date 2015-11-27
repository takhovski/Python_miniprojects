# 2. Guess the Number
import random

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
number = random.randint(1,100)
print("I did!")
condition = True
while condition == True:
    temp = int(input("Guess my number. Good Luck!"))
    condition = compare(temp,number)
    
