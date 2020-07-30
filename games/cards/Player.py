from games.cards.DeckOfCards import DeckOfCards
from games.cards.Card import Card
import random
#מחלקת שחקן-מכילה את השם, כמות כסף וקלפים
class Player:
    #מתודת הקונסטרקטור של המחלקה player
    def __init__(self,name,money,cardamount=5):
        self.name=name
        self.money=money
        self.cardamount=cardamount
        self.cards=[]
    #מתודה המקבלת חבילת קלפים חדשה עבור שחקן
    def setHand(self,dcards):
        for i in range(0,self.cardamount):
            self.cards.append(dcards.dealOne())
    #מתודה המושכת קלף אקראי מהשחקן
    def getCard(self):
        i=random.randint(0,self.cardamount-1)
        card=self.cards.pop(i)
        self.cardamount-=1
        return card
    #מתודה המוסיפה קלף לחפיסה
    def addCard(self,card):
        self.cards.append(card)
        self.cardamount+=2
    #מתודה המורידה כסף מקופת השחקן
    def reduceAmount(self,money):
        self.money=self.money-money
    #מתודה המוסיפה כסף לשחקן
    def addAmount(self,money):
        self.money=self.money+money
    #מתודה repr של המחלקה
    def __repr__(self):
        return f'The name of the player is:{self.name}, the money of the player is: {self.money}, the cards amount is:{self.cardamount}, the cards of the player are: {self.cards}'
    #מתודת הדפסה של פרטי השחקן
    def print(self):
        print(Player.__repr__(self))
