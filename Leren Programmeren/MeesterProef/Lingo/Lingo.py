from lingowords import words
import random
from colorama import Fore, Style


def selectWords(words):
    return random.choice(words)


def userInput():
    while True:
        guess = input(Fore.WHITE + "Raad: " + Style.RESET_ALL).lower()
        if len(guess) > 5:
            print("Alle woorden zijn maar 5 letters lang")
        elif len(guess) < 5:
            print("Alle woorden zijn 5 letters lang")
        elif any(chr.isdigit() for chr in guess): # chr = character
            print("Je mag geen nummers invoeren")    
        else:
            return guess

        
def mainGame():
    wordToGuess = selectWords(words)
    print(wordToGuess)
    correct_positions = set()
    attempts = 0
    print("Eerste letter is: ",wordToGuess[0])
    for Guesses in range(5):
        attempts += 1
        print(Fore.WHITE + "Poging:" , attempts)
        guess = userInput()
        letter = ""
        correct_guesses = set()
        if guess == wordToGuess:
            return print("Congrats woord was" + Fore.GREEN + wordToGuess)
        elif Guesses == 4:
            return print("Helaas het is je niet gelukt het woord om te raden was: " + Fore.RED + wordToGuess )
        else:
             for i in range(len(guess)):
                
                if guess[i] == wordToGuess[i]:
                    letter += Fore.GREEN + guess[i]
                    correct_guesses.add(guess[i])
                    correct_positions.add(i)
                elif guess[i] in wordToGuess and i not in correct_positions and guess[i] not in correct_guesses:
                    letter += Fore.YELLOW + guess[i]
                    correct_guesses.add(guess[i])
                else:
                    letter += Fore.RED + guess[i]  
        
        print("Laatste raad: " + letter)
        
Run = mainGame()