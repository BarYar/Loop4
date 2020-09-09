from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from unittest import TestCase
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#Ordering 3 items and then checking if the items exist in the cart.
class TestAOS(TestCase):
    #setUp
    def setUp(self):
        path = r"C:\Users\97252\Desktop\Selenium\chromedriver.exe"
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://www.advantageonlineshopping.com/#/")
    def tearDown(self):
        self.driver.quit()
    # Ordering 2 items with different quantities and then checking if the items exist in the cart.
    def test1(self):
        enteredProducts= {}
        cartProducts= {}
        try: #Entering the tablets category.
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "tabletsImg"))
            )
        except:
            self.fail()
        self.driver.find_element_by_id("tabletsImg").click()
        try:#Entering the first product page.
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "17"))
            )
        except:
            self.fail()
        self.driver.find_element_by_xpath("//img[@src='/catalog/fetchImage?image_id=3200']").click()
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[@class='roboto-regular screen768 ng-binding']"))
            )
        except:
            self.fail()
        #Entering the first product to the cart.
        productName=(self.driver.find_element_by_xpath("//h1[@class='roboto-regular screen768 ng-binding']").text)
        actions=ActionChains(self.driver)
        actions.double_click(self.driver.find_element_by_xpath("//div[@class='plus']")).perform()
        enteredProducts[productName]=3
        self.driver.find_element_by_name("save_to_cart").click()
        self.driver.find_element_by_xpath("//a[@class='ng-binding']").click()
        try:#Entering the second product page.
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "18"))
            )
        except:
            self.fail()
        self.driver.find_element_by_id("18").click()
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[@class='roboto-regular screen768 ng-binding']"))
            )
        except:
            self.fail()
        # Entering the second product to the cart.
        productName = (self.driver.find_element_by_xpath("//h1[@class='roboto-regular screen768 ng-binding']").text)
        self.driver.find_element_by_xpath("//div[@class='plus']").click()
        enteredProducts[productName] = 2
        self.driver.find_element_by_name("save_to_cart").click()
        self.driver.implicitly_wait(3)
        #Adding the products in cart to the dictionary.
        table=self.driver.find_element_by_xpath("//table[@ng-show='cart.productsInCart.length > 0']")
        print(table.text)
        item1=table.find_element_by_xpath("/tbody/tr/td[1]")
        item2=table.find_element_by_xpath("/tbody/tr[1]/td[1]")
        cartProducts[item1.find_elements_by_xpath("//h3[@class='ng-binding']").text]=item1.find_elements_by_xpath("//label[@class='ng-binding']").text
        cartProducts[item2.find_elements_by_xpath("//h3[@class='ng-binding']").text] = item2.find_elements_by_xpath( "//label[@class='ng-binding']").text
        print(cartProducts)
if __name__=="__main__":
    unittest.main()

