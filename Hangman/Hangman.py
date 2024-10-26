'''
Hangman.py
Names: [Drake AuClaire, Kalil]
'''

import sys
import random

class Hangman:
    '''
    Initializes the words list
    '''
    def __init__(self):
        file = open('words.txt','r')
        self.words = []
        self.wordguess = []
        for line in file:
            self.words.append(line.rstrip())

    '''
    Outputs the current status of the guesses
    '''
    def printword(self):
        for c in self.wordguess:
            print(c,end="")
        print()

    def is_single_character(self, char):
        if char.isalpha() and len(char) == 1:
            return True

    def char_in_word(self, word, all_guesses, current_guess):
        return list(map(lambda x, y: y if y == current_guess else x, all_guesses, word))

    def playgame(self):
        # generate random word
        word = self.words[random.randint(0,len(self.words)-1)]
        #print word
        self.wordguess = ['_'] * len(word)

        missed = [" "] * 10
        guesses = 0
        all_guesses = set()
        solved = False

        while guesses < 10 and not solved:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print(f"You have {10 - guesses} turns left!")
            print("Word:\t" + " ".join(self.wordguess))
            print("Misses:\t" + " ".join(missed))
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

            current_guess = input('Enter a guess:').lower()
            
            ### Your code goes here:###
            if not self.is_single_character(current_guess):
                print("Guess must be a single letter!")
                continue

            if current_guess in all_guesses or current_guess in missed:
                print("You already guessed this!")
                continue

            all_guesses.add(current_guess)

            new_guess = self.char_in_word(word, self.wordguess, current_guess)

            if self.wordguess == new_guess:
                missed[guesses] = current_guess
                guesses += 1

            self.wordguess = new_guess

            if "_" not in self.wordguess:
                solved = True

        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(f"You have {10 - guesses} turns left!")
        print("Word:\t" + " ".join(self.wordguess))
        print("Misses:\t" + " ".join(missed))
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

        if solved:
            print("Congrats, you solved the word!")
        else:
            print(f"You lost! The word was {word}.")


if __name__ == "__main__":

    game = Hangman()

    game.playgame()
