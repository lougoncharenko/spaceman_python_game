import random


#-------------------------------------------------------------------------------
#A function that reads a text file of words and randomly selects one to use as the secret word 
def choose_secret_word():
    filename = open('words.txt', 'r')
    words_list = filename.readlines()
    filename.close()
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    #print(secret_word)
    return secret_word



#--------------------------------------------------------------------------------
# #    A function that checks if all the letters of the secret word have been guessed.
def is_word_guessed(secret_word, letters_guessed):
    for letter in letters_guessed:
        if letter in secret_word:
            return True

     # TODO: Loop through
     # the letters in the secret_word and check if a letter is not in lettersGuessed
# 
# #--------------------------------------------------------------------------------
# #A function that is used to get a string showing the letters guessed so far in the secret word and underscores 
# # for letters that have not been guessed yet.
# def get_guessed_word(secret_word, letters_guessed):
#      for letter in secret_word:
#         print(letter)
#     #TODO: Loop through the letters in secret word and build a string that shows the letters that 
#     # have been guessed correctly so far that are saved in letters_guessed and underscores for 
#     # the letters that have not been guessed yet
def get_guessed_word(secret_word, letters_guessed):
    print(letters_guessed)
    print(secret_word)



# #--------------------------------------------------------------------------------
# # A function to check if the guessed letter is in the secret word
def is_guess_in_word(guess, secret_word):
    if guess in secret_word:
        print("It's a match")
    else:
        print('No match')



# #--------------------------------------------------------------------------------
# # A function that controls the game of spaceman. Will start spaceman in the command line.
def play_spaceman(secret_word):
    print(secret_word)
    guess = 0
    letters_guessed= []
    while guess < 7:
        userInput = input('Enter a letter to guess: ')
        is_guess_in_word(userInput, secret_word)
        letters_guessed.append(userInput)
        get_guessed_word(secret_word, letters_guessed)
        guess += 1
    if is_word_guessed():
        print('Player Won the game')
    else:
        print('Player Lost Game')
   
        


#These function calls that will start the game
secret_word = choose_secret_word()  
play_spaceman(secret_word)