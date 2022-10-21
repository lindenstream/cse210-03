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
        self.print_player()
        self.is_playing = False

    def print_player(self):
        for i in range(0,len(self.player)):
            print(self.player[i])
    