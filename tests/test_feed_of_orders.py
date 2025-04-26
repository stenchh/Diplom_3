import allure
from pages.feed_of_orders_page import OrdersFeedPage
from pages.personal_account import PersonalAccountPage
from pages.main_page import MainPage
from data import ACCOUNT_DATA

class TestFeedOfOrders:

    @allure.title('Открытие и закрытие заказов')
    @allure.step('Нажать на кнопку ленты заказов и закрыть все заказы')
    def test_open_and_close_orders(self, driver):
        orders_feed_page = OrdersFeedPage(driver)
        main_page = MainPage(driver)

        main_page.click_on_feed_of_orders_button()
        orders_feed_page.open_and_close_all_orders()

        assert orders_feed_page.modal_window_is_not_displayed()

    @allure.feature('Лента заказов')
    @allure.story('Нажать на ленту заказов')
    @allure.step('Нажать на кнопку ленты заказов и проверить URL')
    def test_click_on_orders_feed(self, driver):
        main_page = MainPage(driver)
        current_url = main_page.click_on_feed_of_orders_button()

        assert current_url == 'https://stellarburgers.nomoreparties.site/feed'


    @allure.title('Создать заказ и проверить, что счетчик выполненных сегодня заказов увеличился на 1')
    @allure.step('Создать заказ и проверить, что счетчик выполненных сегодня заказов увеличился на 1')
    def test_create_order_completed_today_orders_count_increased_by_1(self, driver):
        orders_feed_page = OrdersFeedPage(driver)
        main_page = MainPage(driver)
        personal_account = PersonalAccountPage(driver)

        first_check = orders_feed_page.check_complete_today_counter()

        main_page.click_on_personal_account_button()

        personal_account.input_email(ACCOUNT_DATA['email'])
        personal_account.input_password(ACCOUNT_DATA['password'])
        personal_account.click_login_and_wait_for_url_change()

        main_page.move_ingredient_to_container()

        main_page.click_on_order_button()

        main_page.close_order_info()

        main_page.click_on_feed_of_orders_button()

        second_check = orders_feed_page.check_complete_today_counter()

        assert second_check == first_check + 1


    @allure.title('Создать заказ и проверить, что счетчик выполненных заказов увеличился на 1')
    @allure.step('Создать заказ и проверить, что счетчик выполненных заказов увеличился на 1')
    def test_completed_orders_for_all_time(self, driver):
        orders_feed_page = OrdersFeedPage(driver)
        main_page = MainPage(driver)
        personal_account = PersonalAccountPage(driver)

        first_check = orders_feed_page.check_completed_counter()

        main_page.click_on_personal_account_button()

        personal_account.input_email(ACCOUNT_DATA['email'])
        personal_account.input_password(ACCOUNT_DATA['password'])
        personal_account.click_login_and_wait_for_url_change()

        main_page.move_ingredient_to_container()

        main_page.click_on_order_button()

        main_page.close_order_info()

        main_page.click_on_feed_of_orders_button()

        second_check = orders_feed_page.check_completed_counter()

        assert second_check == first_check + 1


    @allure.title('Проверка номера заказа в ленте заказов')
    @allure.step('Создать заказ и проверить, что номер заказа появился в ленте заказов')
    def test_order_number_appears_in_orders_in_word(self, driver):
        orders_feed_page = OrdersFeedPage(driver)
        main_page = MainPage(driver)
        personal_account = PersonalAccountPage(driver)

        main_page.click_on_feed_of_orders_button()
        orders_feed_page.check_empty_orders_in_work()

        main_page.click_on_personal_account_button()
        personal_account.input_email(ACCOUNT_DATA['email'])
        personal_account.input_password(ACCOUNT_DATA['password'])
        personal_account.click_login_and_wait_for_url_change()

        main_page.move_ingredient_to_container()
        main_page.click_on_order_button()

        order_number = orders_feed_page.check_number_of_order()
        main_page.close_order_info()
        main_page.click_on_feed_of_orders_button()

        order_number_in_feed = orders_feed_page.check_number_of_order_order_feed()

        assert order_number == order_number_in_feed

    @allure.title('Сравнение номера заказа в истории с номером заказа в ленте')
    @allure.step('Сравнить номер заказа из истории с номером заказа в ленте')
    def test_compare_order_history_with_feed(self, driver):
        orders_feed_page = OrdersFeedPage(driver)
        main_page = MainPage(driver)
        personal_account = PersonalAccountPage(driver)

        main_page.click_on_personal_account_button()

        personal_account.input_email(ACCOUNT_DATA['email'])
        personal_account.input_password(ACCOUNT_DATA['password'])
        personal_account.click_login_and_wait_for_url_change()

        main_page.move_ingredient_to_container()
        main_page.click_on_order_button()
        main_page.close_order_info()

        main_page.click_on_personal_account_button()
        personal_account.click_order_history()
        my_order_history = personal_account.get_last_order_number()

        main_page.click_on_feed_of_orders_button()
        orders_feed = orders_feed_page.get_order_number_from_feed()

        assert my_order_history == orders_feed
