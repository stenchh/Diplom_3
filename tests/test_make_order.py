import allure
from pages.personal_account import PersonalAccountPage
from pages.main_page import MainPage

class TestMakeOrder:

    @allure.title("Авторизация и оформление заказа")
    @allure.step("Авторизация и оформление заказа с проверкой всплывающего окна")
    def test_authorize_and_take_order(self, driver):
        personal_account = PersonalAccountPage(driver)
        main_page = MainPage(driver)

        driver.get("https://stellarburgers.nomoreparties.site/")
        main_page.click_on_personal_account_button()

        allure.attach("Email", "shagova14764@yandex.ru")
        allure.attach("Password", "123456")

        personal_account.input_email('shagova14764@yandex.ru')
        personal_account.input_password('123456')
        personal_account.click_login_and_wait_for_url_change()

        main_page.click_on_order_button()

        assert main_page.pop_up_window_is_dispayed()

    @allure.title("Закрытие всплывающего окна")
    @allure.step("Закрытие всплывающего окна и проверка доступности кнопки заказа")
    def test_close_pop_up_window(self, driver):
        personal_account = PersonalAccountPage(driver)
        main_page = MainPage(driver)

        driver.get("https://stellarburgers.nomoreparties.site/")
        main_page.click_on_personal_account_button()

        allure.attach("Email", "shagova14764@yandex.ru")
        allure.attach("Password", "123456")

        personal_account.input_email('shagova14764@yandex.ru')
        personal_account.input_password('123456')
        personal_account.click_login_and_wait_for_url_change()

        main_page.click_on_order_button()

        main_page.close_pop_up_window()

        assert main_page.order_button_is_displayed()
