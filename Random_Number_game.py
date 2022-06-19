#import the random module
import random

#create a variable for the random number
number = random.randint(0, 100)

end_of_game = False #as log as this is false the While loop will continue to loop until the conditions are met.

while  not end_of_game:
    user_input = int(input("Guess the random number: ")) #create a variable that allows user input
    n = user_input #give the user_input a variable to make it easier to call
    if n < number: #this if statement will give conditions to the while loop
        print("Nope! Higher!")
    elif n > number:
        print("Nope! Lower!")
    elif n == number:
        end_of_game = True #this implies that once the random number and the user imput matches the game will end
        print(f"You got it! the number was" + " " + str(number) + "!")
    
