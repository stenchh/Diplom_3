import allure
from pages.reset_password import ResetPasswordPage
from data import ACCOUNT_DATA

class TestResetPassword:

    @allure.story("Переход на страницу восстановления пароля")
    @allure.step("Переход на страницу восстановления пароля")
    def test_move_to_reset_pass_page(self, driver):
        reset_password = ResetPasswordPage(driver)

        current_url = reset_password.click_reset_password()

        assert current_url == 'https://stellarburgers.nomoreparties.site/forgot-password'

    @allure.story("Сброс пароля с использованием email")
    @allure.step("Ввод email для сброса пароля и проверка отображения поля пароля")
    def test_reset_pass_with_email(self, driver):
        reset_password = ResetPasswordPage(driver)
        reset_password.click_reset_password()
        reset_password.input_email_and_reset(ACCOUNT_DATA['email'])

        assert reset_password.password_input_is_displyaed()

    @allure.story("Активация поля ввода пароля при клике")
    @allure.step("Клик по полю пароля и активация поля ввода пароля")
    def test_activate_pass_button_through_click(self, driver):
        reset_password = ResetPasswordPage(driver)
        reset_password.click_reset_password()
        reset_password.input_email_and_reset(ACCOUNT_DATA['email'])
        reset_password.password_input_becomes_active_through_click()

        assert reset_password.password_input_is_active()

    @allure.story("Активация поля ввода пароля через иконку глаза")
    @allure.step("Клик по иконке глаза для отображения пароля")
    def test_activate_pass_button_through_eye(self, driver):
        reset_password = ResetPasswordPage(driver)
        reset_password.click_reset_password()
        reset_password.input_email_and_reset(ACCOUNT_DATA['email'])
        reset_password.password_input_active_eye_click()

        assert reset_password.password_input_is_active()
