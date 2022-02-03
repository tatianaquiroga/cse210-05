#from game.jumper import Jumper
#from game.word import Word
#from game.terminal import Terminal

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
        while self._is_playing:
            pass