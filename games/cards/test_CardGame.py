from games.cards.CardGame import CardGame
from unittest import TestCase,mock
from unittest.mock import patch
from games.cards.DeckOfCards import DeckOfCards
from games.cards.Card import Card
from games.cards.Player import Player
from games.cards.CardGame import CardGame
class TestCardGame(TestCase):
#מתודת הsetup
    def setUp(self):
        self.game=CardGame(5500,6)
#מתודה שבודקת אם הוא מאתחל את המשתנים
    def test_init1(self):
        self.assertTrue(self.game.cardsAmount==6)
        self.assertTrue(self.game.money==5500)
#מתודה שבודקת שהוא מעלה תקלה כאשר הוא מזין כמות כסף שלילית.
    def test_negetive_money(self):
        try:
            game=CardGame(-100)
        except:
            pass
        else:
            self.fail()
#מתודה שבודקת שהוא מעלה תקלה כאשר המשתמש מזין כמות קלפים לא חוקית
    def test_negetive_cards_amount(self):
        try:
            game=CardGame(5500,-5)
        except:
            pass
        else:
            self.fail()
#פונקציה הבודקת שהמשחק מאתחל את כמות הקלפים לכל השחקנים
    def test_new_game1(self):
        for i in range(0,len(self.game.players)):
            self.assertTrue(len(self.game.players[i].cards)==6)
#פונקציה הבודקת שהמשחק מאתחל את את המשתנה cards amount לכל השחקנים
    def test_new_game2(self):
        for i in range(0,len(self.game.players)):
            self.assertTrue(len(self.game.players[i].cardamount) == 6)

