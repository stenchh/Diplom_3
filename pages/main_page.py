import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, "p.AppHeader_header__linkText__3q_va.ml-2:nth-of-type(1)")
    FEED_OF_ORDERS_BUTTON = (By.CSS_SELECTOR, "p.AppHeader_header__linkText__3q_va.ml-2:nth-of-type(2)")
    PERSONAL_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a.AppHeader_header__link__3D_hX:nth-child(3) > p:nth-child(2)")
    ORDER_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")
    POP_UP_WINDOW = (By.CLASS_NAME, "Modal_modal__contentBox__sCy8X")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK")

    @allure.step("Нажать на кнопку 'Лента заказов'")
    def click_on_feed_of_orders_button(self):
        self.click_element(self.FEED_OF_ORDERS_BUTTON)
        self.wait_for_url("https://stellarburgers.nomoreparties.site/feed")

    @allure.step("Нажать на кнопку 'Конструктор'")
    def click_on_constructor_button(self):
        self.click_and_wait(self.CONSTRUCTOR_BUTTON, self.ORDER_BUTTON)

    @allure.step("Нажать на кнопку 'Личный кабинет'")
    def click_on_personal_account_button(self):
        self.find_element(self.PERSONAL_ACCOUNT_BUTTON)
        self.click_element(self.PERSONAL_ACCOUNT_BUTTON)
        self.wait_for_url("https://stellarburgers.nomoreparties.site/login")

    @allure.step("Нажать на кнопку 'Заказать'")
    def click_on_order_button(self):
        self.click_element(self.ORDER_BUTTON)
        self.find_element(self.POP_UP_WINDOW)

    @allure.step("Проверить, отображается ли всплывающее окно")
    def pop_up_window_is_dispayed(self):
        return self.find_element(self.POP_UP_WINDOW).is_displayed()

    @allure.step("Закрыть всплывающее окно")
    def close_pop_up_window(self):
        self.find_element(self.CLOSE_BUTTON)
        self.click_element(self.CLOSE_BUTTON)
        self.find_element(self.ORDER_BUTTON)

    @allure.step("Проверить, отображается ли кнопка 'Заказать'")
    def order_button_is_displayed(self):
        return self.find_element(self.ORDER_BUTTON).is_displayed()
