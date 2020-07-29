class Card:
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit
    def __repr__(self):
        return f'The value of the card is:{self.value}, the suit is:{self.suit}.'
