from selenium import webdriver
import unittest

from pages import CoffeeCartPage, BasePage
from pprint import pprint as print

URL = "https://coffee-cart.app/"


class CoffeeCartTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        oprtions = webdriver.ChromeOptions()
        oprtions.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(options=oprtions)
        cls.driver.get(url=URL)

    def setUp(self):
        self.driver.get(url=URL)
        self.home = CoffeeCartPage(self.driver).

    def test1(self):
        text = self.home.totalBtn.text
        self.assertEqual(text, "Total: $0.00")


if __name__ == "__main__":
    unittest.main()
