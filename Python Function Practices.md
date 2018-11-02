# Python Function Practices

Author: Jamesong7822

Updated As Of: 03/11/2018

## 1. Guess The Number

Program a function that lets the computer randomly select a number, and allows the player 5 tries to guess it. After each guess, the computer passes a hint to the player (*Too High or Too Low*). 

Hint: Make use of the random library's randint module

## Loops Practice

### A

```python
# Iterate through this given number list and write function(s) that do the described taskings

data = [-20, 71, 30, -87, -89, 39, 61, 64, 95, 87, 19, -95, 63, -78, 44, -91, -78, -77, 19, 26, 39, 3, 78, -39, -18, 18, 90, 75, -3, 9, -17, -96, 95, -100, 38, 40, -89, 86, -11, -79, -24, -85, -6, 13, -86, -21, 29, 64, 94, -24, -48, 21, -44, 96, 10, -28, 46, -80, 61, 17, 73, -46, -28, -51, -58, 26, -51, 14, 32, -73, 5, 82, 59, -70, 78, 39, -16, 51, -63, 99, -43, -24, -65, 20, 78, 0, 47, 45, 74, 1, -72, -2, 98, 25, 26, -26, -39, -59, -95, 51]

# Write a function to return 2 lists, an even number and odd number list
def even_odd_sort():
    pass
	# Even = [-20, 30, 64, -78, 44, -78, 26, 78, -18, 18, 90, -96, -100, 38, 40, 86, -24, -6, -86, 64, 94, -24, -48, -44, 96, 10, -28, 46, -80, -46, -28, -58, 26, 14, 32, 82, -70, 78, -16, -24, 20, 78, 0, 74, -72, -2, 98, 26, -26]
    
    # Odd = [71, -87, -89, 39, 61, 95, 87, 19, -95, 63, -91, -77, 19, 39, 3, -39, 75, -3, 9, -17, 95, -89, -11, -79, -85, 13, -21, 29, 21, 61, 17, 73, -51, -51, -73, 5, 59, 39, 51, -63, 99, -43, -65, 47, 45, 1, 25, -39, -59, -95, 51]

# Write a function that takes in 2 inputs(a,b), where a < b to return all numbers between a and b inclusive
def between_range(a,b):
    pass

```

## Recursion 

Recursion is simply the practice of a function calling itself (or a series of functions) in a cycle. *ie. A to B to C to A*

```python
# Fibonacci Generator
# Define a function that takes in an integer input n, and returns the nth fibonacci number.
def fibo(n):
    pass
# However, why is this method not recommended?
```

# Solutions

## S1. Guess The Number

```python
# Import the necessary randint module from random library
from random import randint

# Defines my function - which I am going to call 'Guess'
def guess():
    # Let computer choose a random number (from 1 - 100) - and assign to var ans
    ans = randint(1, 101) 
    
    # Sets up 2 variables
    # A max try threshold value
    max_num_of_tries = 5
    # A var to count number of tries so far
    num_of_tries = 1
    
    # Sets up a while loop to iterate each guess loop, which runs only when you have tries remaining
    while num_of_tries <= max_num_of_tries:
        print("Guess a Number from 1 to 100!")
        
        # Takes in input from user - stored in user_guess var
        user_guess = int(input("Try Num {} --> Tell me your guess >>>".format(num_of_tries)))
        
        # Hints - conditionals
        if user_guess > ans:
            print("Guess is too HIGH")
            
        elif user_guess < ans:
            print("Guess is too LOW")
            
        else:
            print("Congratulations! You guessed correctly in {} tries.".format(num_of_tries))
            # Immediately break out of the function
        return
        
        # Increment the num_of_tries var by 1 to indicate end of each loop of the game
        num_of_tries += 1
        
    # If you didnt guess correctly within 5 tries, you would break out of the while loop. Here you put in stuff that runs when you didnt win the game
    print("HA YOU SUCK, U DIDNT GUESS CORRECTLY!")
    print("The correct answer is {}. YOU FOOL!".format(ans))
    
# Of course, nothing will run if you dont call the function!
guess()
```

Notice, this function does not take in inputs. What kind of inputs can we use to make the function more mouldable by the user?

```python
# Imports
from random import randint

def guess2(max_tries, range1, range2):
    """
    This improved function allows the user to set parameters for his game
    """
    
    # Randomise choice from range1 to range2
    ans = randint(range1, range2+1)
    
    # Set up variables to check/update during the game loop
    try_count = 1
    
    # Game loop
    while try_count <= max_tries:
        print("Guess a Number from {} to {}. You have {} tries left".format(range1, range2, max_tries - try_count + 1))
        
        # Takes in input from user
        user_guess = int(input("Try {} --> Guess:  ".format(try_count)))
        
        # Hints
        if user_guess < ans:
            print("Too Low")
        elif user_guess > ans:
            print("Too High")
        else:
            print("Congrats! That took {} tries!".format(try_count))
            # Quit out of function
            return
        # Increment try_count by 1
        try_count += 1
        
    print("Boo, you SCRUB. My secret number is {}!!".format(ans))
    
# Call the function with user set params
max_tries = int(input("Max Tries: "))
range1 = int(input("Guess range from: "))
range2 = int(input("to: "))
guess2(max_tries, range1, range2)
```

