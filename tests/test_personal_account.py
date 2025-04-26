import allure
from pages.main_page import MainPage
from pages.personal_account import PersonalAccountPage
from data import ACCOUNT_DATA

class TestPersonalAccount:

    @allure.title("Переход в личный кабинет")
    @allure.step("Переход на страницу личного кабинета")
    def test_go_to_personal_account(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_personal_account_button()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    @allure.title("Переход в историю заказов")
    @allure.step("Переход в историю заказов после авторизации")
    def test_go_to_order_history(self, driver):
        personal_account = PersonalAccountPage(driver)
        main_page = MainPage(driver)

        main_page.click_on_personal_account_button()

        personal_account.input_email(ACCOUNT_DATA['email'])
        personal_account.input_password(ACCOUNT_DATA['password'])
        personal_account.click_login_and_wait_for_url_change()


        main_page.click_on_personal_account_button()
        personal_account.click_order_history()


        assert "/account/order-history" in personal_account.get_current_url()

    @allure.title("Выход из личного кабинета")
    @allure.step("Выход из личного кабинета и проверка редиректа")
    def test_logout(self, driver):
        personal_account = PersonalAccountPage(driver)
        main_page = MainPage(driver)

        main_page.click_on_personal_account_button()


        personal_account.input_email(ACCOUNT_DATA['email'])
        personal_account.input_password(ACCOUNT_DATA['password'])
        personal_account.click_login_and_wait_for_url_change()


        main_page.click_on_personal_account_button()
        current_url = personal_account.click_logout_and_check_redirect()


        assert current_url == "https://stellarburgers.nomoreparties.site/"
