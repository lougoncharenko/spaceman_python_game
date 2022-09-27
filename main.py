from fileinput import filename
import random

def choose_secret_word():
    filename = open('words.txt', 'r')
    words_list = filename.readlines()
     
    # for word in words_list:
    #     print(word, end = '')
    
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    #print(secret_word)
    return secret_word

def play_spaceman(secret_word):
    print(secret_word)


#These function calls that will start the game
secret_word= choose_secret_word()   
play_spaceman(secret_word)