from games.cards.CardGame import CardGame
import random
import time
import tkinter as tk
import smtplib, ssl
#פונקציה המוציא את הקלף הכי גדול
#משחק מלחמה
money = random.randint(5000, 10000)
game=CardGame(money)
port = 465  # For SSL
# Create a secure SSL context
context = ssl.create_default_context()
b=False
#שולח מייל עם הקלפים לשחקנים.
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    while not b:
        try:
            password = input("Type your password and press enter: ")
            server.login("card.game1j@gmail.com", password)
        except:
            print("Invalid password.")
        else:
            b=True
    sender_email = "card.game1j@gmail@gmail.com"
    for i in range(0,4):
        message=game.players[i].cards.__repr__().encode('utf-8')
        #message=message,f'{message},{i},{str(c)}'
        #message = f'Hey {game.players[i].name} your cards are: {c}'.encode('utf-8')
        server.sendmail(sender_email,game.players[i].mail,message)
        #@gmail.com
round=1
roundmoney=0
cards=[]
rcards={}
max1=0
max2=0
#חלון המשחק
window=tk.Tk()
window.geometry("1000x1000")
window.title("War Game")
#window.iconbitmap(r'C:\Users\97252\PycharmProjects\Loop4\games\cards\game icons\Joker.ico')
welcome = tk.Label(text="The War Game!", fg="green",height=8, width=15,font=(1,15))
welcome.place(x=325,y=0)
lframe= []
lbutton=[]
lplayerst=[]
for i in range(0,1):
    lframe.append(tk.Frame(window))
    lplayerst.append(tk.Label(lframe[i],text=f'Name:{game.players[i].name} Money:{game.players[i].money} ',height=10,width=30,font=(1,15)))
    lplayerst[i].place(x=325,y=i+1*175)
    for j in range(0,5):
        lbutton.append( tk.Button(lframe[i], text=str(j+1)))
        lbutton[j].place(x=325,y=i+1*175)
        lbutton[j].config(height=5, width=5)
    lframe[i].grid(row=2, column=5)
window.mainloop()
for i in range(0,5):
    roundmoney=round*100*4
    for j in range(0,4):
        card=game.players[j].getCard()
        cards.append(card)
        rcards[game.players[j].name]=card
        game.players[j].reduceAmount(100)
    if(cards[0]>(cards[1])):
        max1=0
    else:
        max1=1
    if (cards[2]>(cards[3])):
        max2 = 2
    else:
        max2 = 3
    if(cards[max1]>(cards[max2])):
        pass
    else:
        max1=max2
    game.players[max1].addAmount(roundmoney)
    print (f'The round winner is: {game.players[max1].name}.\nHe has {game.players[max1].money} ILS')
    print(rcards)
    print("                                                                                        \n----------------------------------------------------------------------------------------\n----------------------------------------------------------------------------------------\n                                                                                        ")
    roundomney=0
    round += 1
    cards.clear()
    time.sleep(5)
max=0
winners=[]
for i in range (0,4):
    if(game.players[i].money>max):
        winners.clear()
        winners.append(game.players[i])
        max=game.players[i].money
    elif (game.players[i].money == max):
        winners.append(game.players[i])
s=' is'
if(len(winners)>1):
    s='s are'
print(f'The winner{s}:',end='')
for i in range(0,len(winners)):
    print (f'Name:{winners[i].name}, Money:{winners[i].money} ILS.')




