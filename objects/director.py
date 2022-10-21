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
        self.word.showProgress()
        self.guess = self._validate_input()

    def _do_updates(self):
        # update word
        # update parachute
        if not self.word.change_answer(self.guess):
            self.parachute.lost_life()
        # check player
        if self.parachute.lives == 0:
            self.player.change_head()
            print("Game over, go walk it off....")
        
        if self.word.actual_letters == self.word.answer:
            self.word.showProgress()
            print("\n\nWhoo Hoo! You live to walk another day!")
            self.player.is_playing = False
        

    def _do_outputs(self):
        # print current guesses
        self.word.showGuesses()
        

    def _validate_input(self):
        validated = False
        while not validated:
            player_guess = input("\nGuess a letter: ").lower()
            if len(player_guess) == 1:
                if ord(player_guess) in range(97,123):
                    validated = True
                else:
                    print("That was not a letter. Try again!")
            else:
                print("Only one character, please. Try again!")
        return player_guess
