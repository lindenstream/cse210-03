from objects.parachute import Parachute
from objects.word import Word
from objects.player import Player

class Director:
    
    def __init__(self):
        self.word = Word()
        self.parachute = Parachute()
        self.player = Player()

    def start_game(self):
        while self.player.is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        self.parachute.print_chute()
        self.player.print_player()
        
        pass

    def _do_updates(self):
        # update word
        # update parachute
        # check player
        pass

    def _do_outputs(self):
        # print confirmation statement
        # print current guesses
        # validate guess against ascii number
        pass

    def _validate_input(self):
        validated = False
        while not validated:
            player_guess = input("Guess a letter: ").lower
            if len(player_guess) == 1:
                if ord(player_guess) in range(97,123):
                    validated = True
                else:
                    print("That was not a letter. Try again!")
            else:
                print("Only one character, please. Try again!")
        return player_guess
