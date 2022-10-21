'''
Has list of words
Randomly pick from words
Update the answer list with guesses

'''
import random

class Word:
    
    def __init__(self):
        self.word_list =[ 'dog', 'long', 'black',
        'phone', 'friendly', 'stage', 'alike', 'leap', 'point',
        'adjust', 'rated', 'space', 'planet', 'drink']
        self.guess_letters = []
        self.actual_letters = []
        self.answer = []
        random.shuffle(self.word_list)
        self.word = self.word_list[-1]
        self.word_length = len(self.word)
        self._create_answer()
        self._create_letters()

    def _create_answer(self):
        for i in range(self.word_length):
            self.answer.append('_ ')

    def _create_letters(self):
        for i in range(self.word_length):
            self.actual_letters.append(self.word[i])

    def change_answer(self, guess):
        if guess in self.guess_letters:
            print('Letter already guessed! Try again.')
            return False
        elif guess in self.actual_letters:
            self.index = self.actual_letters.index(guess)
            self.answer[self.index] = guess
            self.guess_letters.append(guess)
            return True
        else:
            self.guess_letters.append(guess)
            return False
            

        

    def showProgress(self):
        for i in range(self.word_length):
            print(self.answer[i], end=" ")

    def showGuesses(self):
        print("You have guessed: ", end="")
        for i in range(len(self.guess_letters)):
            print(self.guess_letters[i], end=" ")