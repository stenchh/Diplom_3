import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, "p.AppHeader_header__linkText__3q_va.ml-2:nth-of-type(1)")
    FEED_OF_ORDERS_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    PERSONAL_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a.AppHeader_header__link__3D_hX:nth-child(3) > p:nth-child(2)")
    ORDER_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")
    POP_UP_WINDOW = (By.CLASS_NAME, "Modal_modal__contentBox__sCy8X")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK")
    INGREDIENT_ELEMENTS = (By.CLASS_NAME, "BurgerIngredient_ingredient__text__yp3dH")
    ORDER_BASKET = (By.CLASS_NAME, "BurgerConstructor_basket__listContainer__3P_AM")
    MODAL_WINDOW = (By.CLASS_NAME, "Modal_modal__title__2L34m")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]") #По-другому не вышло, только через XPATH проходили тесты
    FILLINGS_TAB = (By.CLASS_NAME, "tab_tab__1SPyG")
    ORDER_INFO = (By.CLASS_NAME, "Modal_modal__container__Wo2l_")
    CLOSE_ORDER_WINDOW_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close__TnseK']")
    COUNTER_LOCATOR = (By.CSS_SELECTOR, ".counter_counter__ZNLkj .counter_counter__num__3nue1")


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


    @allure.step("Проверить, отображается ли таб с начинками")
    def fillings_tab_is_displayed(self):
        return self.find_element(self.FILLINGS_TAB).is_displayed()

    @allure.step('Перемещение ингредиента в конструктор бургера')
    def move_ingredient_to_container(self):
        ingredient = self.find_element(self.INGREDIENT_ELEMENTS)
        basket = self.find_element(self.ORDER_BASKET)

        self.drag_and_drop(ingredient, basket)

    @allure.step('Открыть состав игредиентов и закрыть окно')
    def open_and_close_all_indredients(self):
        ingredients = self.find_elements(self.INGREDIENT_ELEMENTS)
        ingredient_count = len(ingredients)

        for i in range(ingredient_count):
            ingredients = self.find_elements(self.INGREDIENT_ELEMENTS)

            self.find_and_click(self.INGREDIENT_ELEMENTS, index=i)
            self.wait_until_visible(self.MODAL_WINDOW, timeout =5)

            self.click_element(self.MODAL_CLOSE_BUTTON)
    @allure.step('Закрыть окно с информацией о заказе')
    def close_order_info(self):
        self.wait_until_visible(self.ORDER_INFO)
        self.click_element(self.CLOSE_ORDER_WINDOW_BUTTON)

    @allure.step('Проверить увеличение каунтера при добавлении игредиента')
    def check_counter_increases(self):
        ingredients = self.find_elements(self.INGREDIENT_ELEMENTS)
        for ingredient in ingredients:
            initial_counter_value = int(self.find_element(self.COUNTER_LOCATOR).text.strip())


            basket = self.find_element(self.ORDER_BASKET)
            self.drag_and_drop(ingredient, basket)


            self.wait_until_visible(self.COUNTER_LOCATOR, timeout=5)

            updated_counter_value = int(self.find_element(self.COUNTER_LOCATOR).text.strip())

