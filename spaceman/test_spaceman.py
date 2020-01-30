import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
        string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    counter = 0
    for i in secret_word:
        if i in letters_guessed:
            counter += 1
    
    if counter == len(secret_word):
        return True
    else:
        return False




def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    display = ""

    for i in secret_word:
        if i in letters_guessed:
            display += i
        else:
            display += " _ "
    return display

    

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word

    return guess in secret_word

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
    secret_word (string): the secret word to guess.
    '''

    #TODO: show the player information about the game according to the project spec
    print ('''Welcome to Spaceman! You have been given a random secret word to guess. You have 7 chances to guess all of the letters in the secret word. If you guess more than 7 random letters incorrectly, you lose. If guessed correctly, you win!''')
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    letters_guessed = []
    life = 7
    while life > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        guess = input ("Guess a letter ")
        print("You have " + str(life) + " guesses") 
        letters_guessed.append(guess)

        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        correct = is_guess_in_word(guess, secret_word)
        if correct:
            print ("Nice job!")
        else:
            print ("Nice try! Guess again")
            life -= 1

        
        #TODO: show the guessed word so far
        print (get_guessed_word(secret_word, letters_guessed))
        
        #TODO: check if the game has been won or lost
        is_word_guessed (letters_guessed, secret_word)


    if life == 0:
        print ("You lost!")
        print ("the secret word was " + secret_word + "!")
    if life > 0:
        print ("You win!")
        
        
play_again = "Y" 
while play_again == "Y":
    
    secret_word = load_word()
    spaceman(secret_word)

    play_again = input("to play again type 'Y', if not press any key.\n")
print ("Thanks for playng!")

# Test Functions

class spaceman_Tests(unittest.TestCase):
    def test_is_word_guessed(self):   
        self.assertEqual(is_word_guessed("cat", "act"), True)

    def test_get_guessed_word_false(self):
        self.assertEqual(is_word_guessed("cat", "walalalal"), False)

    def test_is_guess_in_word(self):
        self.assertEqual(is_guess_in_word("banana", "d"), False)
    
   





#These function calls that will start the game

unittest.main()