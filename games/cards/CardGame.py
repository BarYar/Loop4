from games.cards.DeckOfCards import DeckOfCards
import random
from games.cards.Card import Card
from games.cards.Player import Player
#מחלקת משחק קלפים-בכל משחק יש 4 שחקנים וחבילת קלפים אחת
class CardGame:
    #פונקציית הקונסטרקטור של המחלקה-מקבלת כפרמטר את כמות הקלפים שכל שחקן מקבל
    def __init__(self,money,cardsAmount=5):
#יכולים להזין כמות קלפים גדולה מהחפסיסה כי זה תלוי במשחק.
        if(type(cardsAmount)==int):
            if(cardsAmount>=0):
                self.cardsAmount=cardsAmount
            else:
                raise ValueError("You've typed an invalid amount of cards.")
        else:
            raise ValueError("You've entered an invalid type for amount of cards.")
        if(type(money)==int):
            if(money>=0):
                self.money=money
            else:
                raise ValueError("You've entered an invalid amount of money.")
        else:
            raise ValueError("You've entered an invalid type for money.")
        self.deckCards = DeckOfCards()
        CardGame.playersPersonalInformation(self)
        CardGame.newGame(self)
    #מתודה המתחילה משחק חדש.
    def newGame(self):
        self.deckCards.newGame()
        for i in range(0,4):
            self.players[i].cardamount=self.cardsAmount
            self.players[i].setHand(self.deckCards)
        CardGame.print(self)
    #מתדוה שמקבלת מהמשתמש את הפרטים האישיים של כל השחקנים.
    def playersPersonalInformation(self):
        self.players=[]
        namevalid=False
        name=""
        print("Let's start the game.\n But first you new to enter your 4 players information.")
        for i in range (0,4):
            print(f'Lets start with player number {i+1} insert his name.')
            while(namevalid==False):
                name=input("Insert his name.")
                if(name!=""):
                    namevalid=True
            player=Player(name,self.money)
            self.players.append(player)
            namevalid=False
            name=""
    #מתודת הדפסה של המשחק קלפים
    def print(self):
        for i in range (0,4):
            print (f'His name is:{self.players[i].name},He has:{self.players[i].money} ILS .\n His cards are:{self.players[i].cards}')

