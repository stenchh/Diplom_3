import allure
from pages.main_page import MainPage

class TestCheckAllIngredients:


    @allure.title('Проверка открытия и закрытия окна контента')
    @allure.step('Открыть и закрыть окно контента с ингредиентами')
    def test_check_open_and_close_content_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_and_close_all_indredients()

        assert main_page.fillings_tab_is_displayed()


    @allure.title('Проверка увеличения счетчика ингредиентов')
    @allure.step('Проверить, что счетчик увеличивается при добавлении ингредиента')
    def test_check_counter_increases(self, driver):
        main_page = MainPage(driver)
        counter_increased = main_page.check_counter_increases()

        assert counter_increased
