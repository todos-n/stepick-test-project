from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    BASKET_LINK_INVALID = (By.CSS_SELECTOR, ".basket-mini a.btn-default_not")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_GOODS = (By.CSS_SELECTOR, "#basket_formset")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

#class MainPageLocators():
    

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME =  (By.CSS_SELECTOR, ".product_main h1")
    MESSAGE_NAME = (By.CSS_SELECTOR, ".alert:first-child strong")
    MESSAGE_SUM = (By.CSS_SELECTOR, ".alert-info strong")



