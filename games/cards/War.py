from games.cards.CardGame import CardGame
import random
import time
#פונקציה המוציא את הקלף הכי גדול
#משחק מלחמה
money = random.randint(5000, 10000)
game=CardGame(money)
round=1
roundmoney=0
cards=[]
rcards={}
max1=0
max2=0
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
    print (f'The round winner is:{game.players[max1].name}.\nHe has {game.players[max1].money} ILS')
    print(rcards)
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




