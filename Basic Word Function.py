from words import wordlist
import random


def get_word():
    word = random.choice(wordlist)
    return word.upper()


def play(word):
  word_complettion = "_" * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 6
  print("Start Hangman.")
  print(display_hangman(tries))
  print(word_complettion)
  print("\n")
 while not guessed and tries > 0:
   guess = input("Guess a letter or word: ").upper()
   if len(guess) == 1 and guess.isalpha():

     elif len(guess) == len(word) and guess.isalpha():
      
    else:
      pring("Not Valid Guess")
    print(display_hangman(tries))
    print("\n")
