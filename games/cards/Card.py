#מחלקה של קלף- לכל קלף יש ערך ומספר
class Card:
    #מתודת הקונסטרקטור של המחלקה
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit
    #מתודת הrepr של המחלקה
    def __repr__(self):
        return f'Value :{self.value}, Suit:{self.suit}.\n'
    #מתודה שבודקת איזה קלף בעל ערך גדול יותר
    def __ge__(self, other):
        suits = ["Club", "Diamond", "Heart", "Spade"]
        values = [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]
        otherv=0
        others=0
        myv=0
        mys=0
        for i in range (0,13):
            for j in range (0,4):
                if (self.value==values[i]):
                    myv=i
                if (self.suit==suits[j]):
                    mys=j
                if (other.value==values[i]):
                    otherv=i
                if (other.suit==suits[j]):
                    others=j
        if (myv>otherv):
            return True
        elif(myv==otherv):
            if(mys>others):
                return True
            else:
                return False
        else:
            return False
