import allure
from pages.personal_account import PersonalAccountPage
from pages.main_page import MainPage
from data import ACCOUNT_DATA

class TestMakeOrder:

    @allure.title("Авторизация и оформление заказа")
    @allure.step("Авторизация и оформление заказа с проверкой всплывающего окна")
    def test_authorize_and_take_order(self, driver):
        personal_account = PersonalAccountPage(driver)
        main_page = MainPage(driver)
        main_page.click_on_personal_account_button()


        personal_account.input_email(ACCOUNT_DATA['email'])
        personal_account.input_password(ACCOUNT_DATA['password'])
        personal_account.click_login_and_wait_for_url_change()

        main_page.click_on_order_button()

        assert main_page.pop_up_window_is_dispayed()

    @allure.title("Закрытие всплывающего окна")
    @allure.step("Закрытие всплывающего окна и проверка доступности кнопки заказа")
    def test_close_pop_up_window(self, driver):
        personal_account = PersonalAccountPage(driver)
        main_page = MainPage(driver)

        main_page.click_on_personal_account_button()

        personal_account.input_email(ACCOUNT_DATA['email'])
        personal_account.input_password(ACCOUNT_DATA['password'])
        personal_account.click_login_and_wait_for_url_change()

        main_page.click_on_order_button()

        main_page.close_pop_up_window()

        assert main_page.order_button_is_displayed()
