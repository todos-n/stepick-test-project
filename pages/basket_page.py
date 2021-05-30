from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_product_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_GOODS), "There are no products in the basket, but should be"
        
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_GOODS), "There are products in the basket, but should not be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "There is no empty basket message, but should be"

    def should_not_be_empty_basket_message(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "There is an empty basket message, but should not be"
