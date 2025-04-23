import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ResetPasswordPage(BasePage):
    LINK_RESET_PASS = (By.LINK_TEXT, "Восстановить пароль")
    PERSONAL_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "p.AppHeader_header__linkText__3q_va.ml-2:nth-of-type(3)")
    INPUT_EMAIL = (By.NAME, "name")
    RESET_PASSWORD_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx")
    INACTIVE_PASSWORD_INPUT = (By.CSS_SELECTOR, "div.input.input_type_password.input_size_default input[type='password']")
    ACTIVE_PASSWORD_INPUT = (By.CSS_SELECTOR, "div.input.input_type_password.input_size_default.input_status_active input[type='password']")
    EYE_ICON = (By.CSS_SELECTOR, "div.input__icon.input__icon-action svg")

    @allure.step("Перейти на страницу восстановления пароля")
    def click_reset_password(self):
        self.click_element(self.PERSONAL_ACCOUNT_BUTTON)
        self.click_element(self.LINK_RESET_PASS)
        self.wait_for_url('https://stellarburgers.nomoreparties.site/forgot-password')

    @allure.step("Ввести email {email} и запросить сброс пароля")
    def input_email_and_reset(self, email):
        self.input_text(self.INPUT_EMAIL, email)
        self.click_element(self.RESET_PASSWORD_BUTTON)

    @allure.step("Кликнуть по полю ввода пароля, чтобы оно стало активным")
    def password_input_becomes_active_through_click(self):
        self.click_element(self.INACTIVE_PASSWORD_INPUT)
        self.wait_until_visible(self.ACTIVE_PASSWORD_INPUT)

    @allure.step("Проверить, что поле ввода пароля активно")
    def password_input_is_active(self):
        return self.find_element(self.ACTIVE_PASSWORD_INPUT).is_displayed()

    @allure.step("Проверить, что поле ввода пароля отображается")
    def password_input_is_displyaed(self):
        return self.find_element(self.INACTIVE_PASSWORD_INPUT).is_displayed()

    @allure.step("Кликнуть по иконке глаза для отображения пароля")
    def password_input_active_eye_click(self):
        self.click_element(self.EYE_ICON)
        self.wait_until_visible(self.ACTIVE_PASSWORD_INPUT)
