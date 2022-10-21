'''
Has a changing head
_______     o
_______    /|\
_______    / \
_______  
_______  ^^^^^^^
Head changes to x
'''

class Player:
    
    def __init__(self):
        self.is_playing = True
        self.player = ['     o',
                       '    /|\ ',
                       '    / \ ',
                       '',
                       '  ^^^^^^^']
    
    def change_head(self):
        self.player[0] = '     x'
        self.is_playing = False

    def print_player(self):
        for i in len(self.player):
            print(self.player[i])
    