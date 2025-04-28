import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PersonalAccountPage(BasePage):
    LINK_RESET_PASS = (By.LINK_TEXT, "Восстановить пароль")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    EMAIL_LABEL = (By.XPATH, "//label[contains(text(), 'Email')]")
    ORDER_HISTORY = (By.CSS_SELECTOR, "a.Account_link__2ETsJ[href='/account/order-history']")
    LOGOUT_BUTTON = (By.CLASS_NAME, "Account_button__14Yp3")
    INPUT_EMAIL = (By.NAME, "name")
    LOGIN_BUTTON =(By.CLASS_NAME, "button_button__33qZ0")
    ORDER_ELEMENT = (By.CLASS_NAME, 'OrderHistory_textBox__3lgbs')
    ORDER_NUMBER = (By.CSS_SELECTOR, '.text_type_digits-default')

    @allure.step("Нажать на кнопку 'Войти' и ждать изменения URL")
    def click_login_and_wait_for_url_change(self):
        self.click_element(self.LOGIN_BUTTON)
        self.wait_for_url('https://stellarburgers.nomoreparties.site/')

    @allure.step("Ввести email: {email}")
    def input_email(self, email):
        self.input_text(self.INPUT_EMAIL, email)

    @allure.step("Ввести пароль: {password}")
    def input_password(self, password):
        self.input_text(self.PASSWORD_INPUT, password)

    @allure.step("Нажать на кнопку 'Выйти' и проверить редирект на главную страницу")
    def click_logout_and_check_redirect(self):
        self.click_element(self.LOGOUT_BUTTON)
        self.wait_for_url("https://stellarburgers.nomoreparties.site/")

    @allure.step("Нажать на ссылку 'История заказов' и ждать редирект на страницу истории заказов")
    def click_order_history(self):
        self.click_element(self.ORDER_HISTORY)
        self.wait_for_url("https://stellarburgers.nomoreparties.site/account/order-history")

    @allure.step('Проверить номер последнего заказа')
    def get_last_order_number(self, timeout=5):
        last_order_number = self.scroll_and_get_last_element_text(self.ORDER_ELEMENT, self.ORDER_NUMBER, timeout)
        return last_order_number.lstrip('#')
