from unittest import TestCase
from W.Worker import Worker
from datetime import datetime

class TestWorker(TestCase):
    import datetime
    def setUp(self):
        print("setup")
        self.bob= Worker ("bob","ma",2020,1,1,"2 Dizengof,Tel Aviv","il")
    def test_full_name(self):
        self.assertTrue(self.bob.first_name == "bob")
    def test_last_name(self):
        self.assertTrue(self.bob.last_name == "ma")
    def test_age(self):
        if(self.bob.birth_year==datetime.now().year):
            if(self.bob.birth_month==datetime.now().month):
                self.assertTrue(self.bob.birth_day<=datetime.now().day)
            else:
                self.assertTrue(self.bob.birth_month<datetime.now().month)
        else:
            self.assertTrue(self.bob.birth_year < 2020)

    def tearDown(self):
        print("tear down")

