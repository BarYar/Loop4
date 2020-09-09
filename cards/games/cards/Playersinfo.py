import tkinter as game
from games.cards.CardGame import CardGame
from games.cards.Card import Card
from games.cards.Player import Player
class playersinfo:
    def __init__(self,players,money):
        self.players=players
        self.money=money
        self.countp=1
        self.window = game.Tk().geometry("60x60")
        welcome = game.Label(text="Let's start the game.\n But first you new to enter your 4 players information.", fg="green").grid(row=1)
        welcome.pack()
        while(self.countp<5):
            self.playersname=game.Entry(text=f'Enter your players names.\nThis is player number {self.countp}.').grid(row=2)
            self.playersname.pack()
            playersbuttun=game.Button(text="Enter",command=playersinfo.ename(self)).grid(row=3)
            playersbuttun.pack()
        self.window.mainloop()
# מתודה המכניסה את שמות השחקנים
    def ename(self):
        name = self.playersname.get()
        self.playersname.delete(0, 'end')
        if (name == ""):
            er = game.Label(text="You need to type a name.", fg="red").grid(row=4)
            er.pack()
        else:
            player = Player(name, self.money)
            self.players.append(player)
            self.countp += 1