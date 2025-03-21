from seleniumpagefactory import PageFactory


class BasePage(PageFactory):

    def __init__(self, driver=None, node=None):
        super().__init__()
        self.driver = driver
        self.node = node


class CoffeeCartPage(BasePage):
    def __init__(self, driver=None, node=None):
        super().__init__(driver, node)
        self.locators = {
            "totalBtn": ("xpath", "//div[@class='pay-container']"),
        }

    def __del__(self):
        print("del")