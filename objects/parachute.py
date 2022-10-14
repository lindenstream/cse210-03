'''
Parachute tracks 4 "lives"
Parachute ASCII art shown and managed (disappear)
List of strings printed:
List @3    ___
List @2   /___\
List @1   \   /
List @0    \ /
_______     o
_______    /|\
_______    / \
_______  
_______  ^^^^^^^
'''

class Parachute:
    
    def __init__(self):
        self.parachute = ['    \ /','   \   /','   /___\ ','    ___']
        self.lives = 4

    def lost_life(self):
        self.parachute = self.parachute[:-1]
        self.lives -= 1
