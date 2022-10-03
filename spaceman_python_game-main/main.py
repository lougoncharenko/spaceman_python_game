"""
SpaceMan Game
"""
import random


#-------------------------------------------------------------------------------
def choose_secret_word():
    """
    description: Function that reads word.txt and randomly selects a word to use.
    Parameter: none
    Returns: A randomly selected secret word 
    """
    filename = open('words.txt', 'r')
    words_list = filename.readlines()
    filename.close()
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

#--------------------------------------------------------------------------------
def is_word_guessed(secret_word, string):
    """
    description:  A function that compares the string with the secret word
    to see if the secret_word was guessed.
    Parameter: secret_word (string), string that is returned from get_guess_word function
    Returns: True or False depending on is the player guessed the secret word.
    """
    if string == secret_word:
        return True
    else:
        return False

##--------------------------------------------------------------------------------

def get_guessed_word(secret_word, letters_guessed):
    """
    description: The function loops through letters guessed and returns a
    string with correct letters guessed and hyphens if for letters not guessed.
    Parameter: secret_word(string) and letters_guessed (an array)
    Returns: A string with letters and hyphens based on what has been guessed so far.
    """
    string = ''
    for letter in secret_word:
        if letter in letters_guessed:
            string += letter
        else:
            string += '_'
    return string

# #--------------------------------------------------------------------------------
def is_guess_in_word(guess, secret_word):
    """
    description: A function to check if the guessed letter is in the secret word
    Parameter: guess (single letter), secret_word(string)
    Returns: A message to the user indicated if they got a match or no match.
    """
    if guess in secret_word:
        print("It's a match")
    else:
        print('No match')



# #--------------------------------------------------------------------------------

def play_spaceman(secret_word):
    """
    description: A function that controls the game of spaceman
    Parameter: secret_word(string)
    Returns: A message to the player if they won or lost the game and displays the secret word
    """
    print(secret_word)
    print ('----------- Welcome To SpaceMan ------------------')
    print ('You have 7 guessed to guess the secret word')
    print ('Each time you guess the right letter, you will see it appear')
    guess = 0
    letters_guessed= []
    while guess < 7:
        string = get_guessed_word(secret_word, letters_guessed)
        print(string)
        user_input = input('Enter a letter to guess: ')
        is_guess_in_word(user_input, secret_word)
        letters_guessed.append(user_input)
        guesses_left = 6 - guess
        print(f'You have {guesses_left} guesses left')
        print(f'Guessed letter: {letters_guessed}')
        guess += 1
    if is_word_guessed(secret_word, string):
        print('Player Won the game')
    else:
        print('Player Lost Game')
        print(f'Secret word is {secret_word}')
#These function calls that will start the game
secret_word = choose_secret_word()
play_spaceman(secret_word)
