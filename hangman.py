## Hangman Game 1.0
## Eric Williams, 2015
## Feel free to edit this in anyway you like!
#Imports
from __future__ import print_function
from sys import exit
#Functions
def init():
    '''Initializes the game'''
    secret = raw_input("Welcome to the Hangman Game!\nPlease enter a secret word/phrase: ")
    if "-" in secret:
        print("'-' is an invalid character. Exiting program.")
        exit()
    print("Thank you. Initializing game...")
    return secret
    
def sort_string(iString):
    '''Sorts a string alphabetically, and removes duplicate characters'''
    newList = []
    newString = ""
    iString = iString.lower() #makes the string lowercase, which is important for the "sort) method on lists
    for letter in iString: 
        if letter != " " and not(letter in newList): #tests if the letter is not already in the list, and that it is not a space
            newList += letter
            newList.sort()
    for letter in newList: #converts the list to a string
        newString += letter
    return newString
    
def get_user_input(userInputs):
    '''Handles user inputs, and makes sure it hasn't already been entered'''
    newInput = str(raw_input("Enter a letter: "))
    newInput = newInput.lower()
    userInputs += newInput #adds the new character to the list
    userInputs = sort_string(userInputs) #alphabatizes the string, and removes duplicates
    return userInputs
    
def create_revealed(secret, userInputs):
    '''Generates the string that shows the correctly guessed characters'''
    revealedList = []
    revealedString = ""
    for letter in secret: 
        if letter.lower() in userInputs or letter.upper() in userInputs:
            revealedList += letter #if the letter has been guesses, it gets revealed
        elif letter == " ":
            revealedList += " " #if the letter is actually a space, it just puts a space in
        else:
            revealedList += "-" #if neither of the conditions is true, the letter is concealed
    for letter in revealedList: #converts the revealedList variable to a string
        revealedString += letter
    return revealedString
    
def wrong_guesses(secret, userInputs):
    '''Figures out how many wrong guesses have been made'''
    numWrong = 0 #clears the numWrong variable, it's really just easier and faster to do
    '''If a guessed letter in the history was not in the secret, it gets added to the newly cleared numWrong variable'''
    for letter in userInputs: 
        if not(letter.lower() in secret) and not(letter.upper() in secret): 
            numWrong += 1
    return numWrong
    
def win_test(secret, userInputs):
    '''Tests if the user has won the game'''
    win = True
    #print("Yeah, win_test runs") (This was used for debugging)
    for letter in secret:
        if (not(letter.lower() in userInputs) and not(letter.upper() in userInputs)) and letter != " ":
            win = False
    return win
            
def draw(numWrong, secret, userInputs):
    '''Procedure for drawing the ASCII Hangman, and writing the info to the screen'''
    hangman = [[ #This set of lists and strings is what the prgram uses to draw the ascii hangman
    " /----|   ",
    " |    |   ",
    " |        ",
    " |         ",
    " |        ",
    " |          ",
    " |        ",
    "----------"],[
    " /----|   ",
    " |    |   ",
    " |    O   ",
    " |         ",
    " |        ",
    " |          ",
    " |        ",
    "----------"],[
    " /----|   ",
    " |    |   ",
    " |    O   ",
    " |    |    ",
    " |    |   ",
    " |          ",
    " |        ",
    "----------"],[
    " /----|   ",
    " |    |   ",
    " |    O   ",
    " |    |    ",
    " |    |   ",
    " |     \    ",
    " |        ",
    "----------"],[
    " /----|   ",
    " |    |   ",
    " |    O   ",
    " |    |    ",
    " |    |   ",
    " |   / \    ",
    " |        ",
    "----------"],[
    " /----|   ",
    " |    |   ",
    " |    O   ",
    " |    |\   ",
    " |    |   ",
    " |   / \    ",
    " |        ",
    "----------"],[
    " /----|   ",
    " |    |   ",
    " |    O   ",
    " |   /|\   ",
    " |    |   ",
    " |   / \    ",
    " |        ",
    "----------"]]
    for layer in hangman[numWrong]:
        '''Goes through each line in the ASCII picture, and prints it.
        If the revelead string or set of past letters should be printed on that line,
        it acts accordingly'''
        outString = layer
        if len(outString) == 11:
            outString += create_revealed(secret, userInputs)
        elif len(outString) == 12:
            if len(userInputs) != 0:
                outString += "You've guessed the following letters: " + userInputs
            else:
                outString += "You have not guessed any letters."
        print(outString)
    return 
    
##Actual code
secret = init() #initializes the game, and stores the secret word/phrase
numWrong = 0 #stores how many wrong guesses have been made
userInputs = "" #stores which letters the user has entered
while numWrong <= 6:
    draw(numWrong, secret, userInputs)
    userInputs = get_user_input(userInputs) #gets a new letter from the user, and updates the list of inputs
    numWrong = wrong_guesses(secret, userInputs) #updates how many wrong guesses there have been
    if win_test(secret, userInputs) == True:
        draw(numWrong, secret, userInputs)
        print("Congratulations! You won in " + str(len(userInputs)) + " guesses!") 
        break
    elif numWrong == 6: #code to run if you lose
        draw(numWrong, secret, userInputs)
        print("Sorry, you lose. The phrase was '" + secret + "'.")
        break
