#from game.jumper import Jumper
#from game.word import Word
#from game.terminal import Terminal
import random
import time
class Director:
    """The player who is playing the game.
    
    Attributes:
        _is_playing (boolean): True if game is still being played
        _lives (int): Number of lives remaining
        _jumper (Jumper): An instance of the Jumper class
        _word (Word): An instance of the Word class
        _terminal (Terminal): An instance of the Terminal class
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): An instance of Director.
        """
        self._is_playing = True

        self._lives = 5
        
        #self._jumper = Jumper()

        #self._word = Word()

        #self._terminal = Terminal()
        
    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        print("Welcome to Jumper Game")
        time.sleep(2)
        print("The puzzle is a secret word randomly chosen from a list.")
        time.sleep(2)
        print("The player guesses a letter in the puzzle.")
        time.sleep(2)
        print("If the guess is correct, the letter is revealed.")
        time.sleep(2)
        print("If the guess is incorrect, a line is cut on the player's parachute.")
        time.sleep(2)
        print("If the puzzle is solved the game is over.")
        time.sleep(2)

        print("If the player has no more parachute the game is over.")
        time.sleep(2)
        
        print("You want to play with words that are car brands or country names?")
        time.sleep(2)
        
        cat_select = input("Enter C for car brands or W for countries: ")

        

        cars = ["ford", "audi", "nissan", "renault", "chevrolet", "mitsubishi", "cadillac", "suzuki"]
        countries= [ "mexico", "colombia", "canada", "venezuela", "uruguay", "argentina",
                            "guatemala", "panama", "ecuador"]

        while True:
            if cat_select.lower() == "c":
                print("Excellent!!, you selected car brands")
                secret_word = random.choice(cars))
                break
            elif cat_select.lower() == "w":
                print("Excellent!!, you selected countries")
                secret_word = random.choice(countries)
                break
        
            else:
                print("Please select a valid category")
                cat_select = input("Enter C for car brands or W for countries: ")
        
        guessed_let = []
        ## We print the word without letters
        print('_' * len(secret_word))
        
        while True:
        
            while True:
                guessed_let = input("Write a letter: ")
                if(len(guessed_let)!=1 and guessed_let.isnumeric()):
                    print("That is not a letter, try with only one letter")
                else:
                    if guessed_let.lower() in guessed_let:
                        print("You already tried with that letter, try with another one")
                    else:
                        guessed_let.append(guessed_let)
        
                        if guessed_let.lower() in secret_word:
                            print("Congratulations!!! That is a correct letter")
                            break
                        else:
                            _lives = _lives-1
                            print("Wrong letter!!! You lose a chance")
                            print("You have  " + str(_lives) + " oportunities")
                            break
        
            if _lives==0:
                print("You lose !!!  The secret word was: : "+ secret_word)
                break
        
        
            status = ""
        
            missing_letters = 0
            for let in secret_word:
        
        
                if let in guessed_let:
                    status = status + let
        
                else:
                    status = status + "_"
                    missing_letters = missing_letters + 1
        
            ## Print word with some letters
            print(status)
        
        
            if missing_letters == 0:
                print("Congratulations !!!!  You win")
                print("The secret word was : " + secret_word)
                break
        






                while self._is_playing:
                    pass