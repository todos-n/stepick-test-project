from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        #проверить есть ли кнопка добавления
        self.should_be_add_to_basket()
        #кликнуть по кнопке
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        #Обработать alert
        self.solve_quiz_and_get_code()
        #есть ли сообщение о добавлении
        self.should_be_adding_message()
        #название совпадает с добавленным
        self.should_be_the_right_name()
        #есть ли сообщение со стоимостью корзины
        self.should_be_sum_message()
        #стоимость совпадает с ценой
        self.should_be_the_right_price()

    def should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket button is not presented"

    def should_be_adding_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_NAME), "Adding message is not presented"

    def should_be_the_right_name(self):
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_NAME).text == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text, "Wrong product name in the message"

    def should_be_sum_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_SUM), "Sum message is not presented"

    def should_be_the_right_price(self):
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_SUM).text == self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text, "Wrong sum in the message"