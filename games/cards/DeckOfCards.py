import random
from games.cards.Card import Card
#מחלקה של רשימה של קלפים, המחלקה תכיל חפיסת קלפים שלמה 13 קלפים מכל סוג-סה"כ 52 קלפים
class DeckOfCards:
    #הקונסטרקטור של המחלקה
    def __init__(self):
        self.__suits=["Club","Diamond","Heart","Spade"]
        self.__values=[ "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]
        DeckOfCards.newGame(self)
    #מתודה המכניסה את הערכים לחבילה.
    def startCards(self):
        for i in self.__values:
            for j in self.__suits:
                card=Card(i,j)
                self.deckcards.append(card)
    #מתדוה פרטית המערבבת את החפיסה
    def _shuffle(self):
        random.shuffle(self.deckcards)
    #מתודה המחזירה את הקלף מראש החפיסה
    def dealOne(self):
        card=self.deckcards.pop()
        return card
    #מתודה המתחילה משחק חדש
    def newGame(self):
        self.deckcards=[]
        DeckOfCards.startCards(self)
        DeckOfCards._shuffle(self)
    #מתודה repr של המחלקה
    def __repr__(self):
        return f'{self.deckcards}'
    #מתודה המדפיסה את כל הקלפים בחפיסה
    def show(self):
        print(DeckOfCards.__repr__(self))




