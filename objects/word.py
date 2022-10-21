'''
Has list of words
Randomly pick from words
Update the answer list with guesses

'''
import random

class Word:
    
    def __init__(self):
        self.word_list =['put words here']
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
        self.guess_letters.append(guess)
        index = self.actual_letters.index(guess)
        self.answer[index] = guess
        return True