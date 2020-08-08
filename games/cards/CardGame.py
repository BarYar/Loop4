from games.cards.DeckOfCards import DeckOfCards
import random
from games.cards.Card import Card
from games.cards.Player import Player
import tkinter as game
import time
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
        self.players=[]
        CardGame.playersPersonalInformation(self)
        CardGame.newGame(self)
    #מתודה המתחילה משחק חדש.
    def newGame(self):
        self.deckCards.newGame()
        for i in range(0,4):
            self.players[i].cardamount=self.cardsAmount
            self.players[i].setHand(self.deckCards)
        CardGame.print(self)
    #מתודה הבודקת את הג'ימייל
    def testmail(self,mail):
        p=0
        for i in range(0,len(mail)):
            if (mail[i]=="@"):
                p=i
                break
        if(p!=0):
            if(mail[p:len(mail)]=="@gmail.com"):
                return True
        return False

    # מתודה המכניסה את שמות השחקנים
    def ename(self):
        name = self.playersname.get()
        mail=self.emailp.get()
        self.er.config(text="")
        self.mer.config(text="")
        if (name == ""):
            self.er.config(text='Type a Password!',fg="red")
        if not self.testmail(mail):
            self.mer.config(text='Invalid mail!',fg="red")
        else:
            self.playersname.delete(0, 'end')
            self.emailp.delete(0, 'end')
            player = Player(name, self.money,mail)
            self.players.append(player)
            self.countp += 1
            self.playersname.delete(0, 'end')
        if (self.countp == 5):
            self.playersbuttun.destroy()
            self.playersname.destroy()
            self.emailp.destroy()
            self.labeln.destroy()
            self.labelm.destroy()
            self.er.destroy()
            self.mer.destroy()
            self.welcome.destroy()
            begin = game.Label(text="Now Let's start the game.")
            begin.grid(row=2,column=1)
            self.window.after(10,lambda :self.window.destroy())
    #מתדוה שמקבלת מהמשתמש את הפרטים האישיים של כל השחקנים.
    def playersPersonalInformation(self):
        # playersinfo(self.players,self.money)
        self.countp=1
        self.window = game.Tk()
        self.window.geometry("400x200")
        self.window.title("War Game")
        self.window.iconbitmap(r'C:\Users\97252\PycharmProjects\Loop4\games\cards\game icons\Joker.ico')
        self.welcome = game.Label(text="Let's start the game.\n But first you need to enter your 4 players information.", fg="green")
        self.welcome.grid(row=1,column=1)
        # time.sleep(5)
        # welcome.destroy()
        self.playersname=game.Entry()
        self.playersname.grid(row=2,column=1)
        self.labeln=game.Label(text="Name:")
        self.labeln.grid(row=2, column=0)
        self.emailp=game.Entry()
        self.emailp.grid(row=3,column=1)
        self.labelm = game.Label(text="Mail:")
        self.labelm.grid(row=3, column=0)
        self.playersbuttun=game.Button(text="Enter",command=self.ename)
        self.playersbuttun.grid(row=4,column=1)
        self.er = game.Label()
        self.er.grid(row=5, column=1)
        self.mer = game.Label()
        self.mer.grid(row=6, column=1)
        self.window.mainloop()
        # namevalid=False
        # name=""
        # print("Let's start the game.\n But first you new to enter your 4 players information.")
        # for i in range (0,4):
        #     print(f'Lets start with player number {i+1} insert his name.')
        #     while(namevalid==False):
        #         name=input("Insert his name.")
        #         if(name!=""):
        #             namevalid=True
        #     player=Player(name,self.money)
        #     self.players.append(player)
        #     namevalid=False
        #     name=""



    #מתודת הדפסה של המשחק קלפים
    def print(self):
        for i in range (0,4):
            print (f'His name is:{self.players[i].name},He has:{self.players[i].money} ILS .\n His cards are:{self.players[i].cards}')

