# def myfunction(a,b,c):
	# # Myfunction checks if any number from 0 - 99 is divisible by a, b and c
	# ans_list = []
	# for i in range(100):
		
		# if i % a == 0 and i % b == 0 and i % c == 0:
			# ans_list.append(i)
	# return ans_list
# print(myfunction(1,2,3))

# D) Write a function that randomly chooses a number from 1 to 100. The player will have to guess \
# correctly within 5 tries for that number, with hints(too small or too big) given

# from random import randint
# def guess():
	# # Let comp choose random number
	# ans = randint(1, 101) # randomise from 1 to 100. Eg. 88
	
	# max_num_of_tries = 5
	# num_of_tries = 1
	
	# while num_of_tries <= max_num_of_tries:
		# print("Guess a Number from 1 to 100")
		# user_guess = int(input("Try Num {}--> Tell me your guess>>".format(num_of_tries)))
		
		# # Hints - conditionals
		# if user_guess > ans:
			# print("Guess is too HIGH")
			
		# elif user_guess < ans: 
			# print("Guess is too LOW")
			
		# else: # same as user_guess == ans
			# print("Congrats You guess correctly in {} tries.".format(num_of_tries))
			# return 
			
		# num_of_tries += 1
	
	# print("HA U SUCK U DIDNT GUESS CORRECTLY")
	# print("The correct ans is {} YOU FOOL!".format(ans))
# guess()

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
