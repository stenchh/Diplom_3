from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class OrdersFeedPage(BasePage):
    ORDER_ITEM = (By.CSS_SELECTOR, "li.OrderHistory_listItem__2x95r a.OrderHistory_link__1iNby")
    MODAL_WINDOW = (By.CSS_SELECTOR, "div.Modal_orderBox__1xWdi.Modal_modal__contentBox__sCy8X")
    MODAL_CLOSE_BUTTON = (By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/button')  # Тут вышло только благодаря использованию полного XPATH, другие локаторы не работали
    COMPLETED_TODAY_COUNTER = (By.CSS_SELECTOR, "p.OrderFeed_number__2MbrQ.text.text_type_digits-large")
    COMPLETED_FOR_ALL_TIME_COUNTER = (By.CSS_SELECTOR, "p.OrderFeed_number__2MbrQ.text.text_type_digits-large")
    WORKING_ORDER = (By.CSS_SELECTOR, "li.text.text_type_digits-default.mb-2")
    NO_ORDERS_MESSAGE = (By.CSS_SELECTOR, "li.text.text_type_main-small")
    ORDER_NUMBER_MODAL = (By.CSS_SELECTOR, "h2.Modal_modal__title_shadow__3ikwq.Modal_modal__title__2L34m.text.text_type_digits-large.mb-8")
    NUMBER_OF_ORDER = (By.CSS_SELECTOR, 'a.OrderHistory_link__1iNby .OrderHistory_textBox__3lgbs p.text_type_digits-default')
    import allure

    class OrdersFeedPage:

        @allure.step('Открыть и закрыть заказ')
        def open_and_close_all_orders(self):
            orders = self.find_elements(self.ORDER_ITEM)
            order_count = len(orders)

            for i in range(order_count):
                orders = self.find_elements(self.ORDER_ITEM)

                self.find_and_click(self.ORDER_ITEM, index=i)
                self.wait_until_visible(self.MODAL_WINDOW, timeout=5)

                self.click_element(self.MODAL_CLOSE_BUTTON)

        @allure.step('Проверить отображение окна')
        def modal_window_is_not_displayed(self):
            element = self.find_element(self.MODAL_WINDOW)
            return not element.is_displayed()

        @allure.step('Получить количество заказов выполненных сегодня')
        def check_complete_today_counter(self, timeout=5):
            return int(self.get_element_text(self.COMPLETED_TODAY_COUNTER, timeout))

        @allure.step('Получить общее количество выполненных заказов')
        def check_completed_counter(self, timeout=5):
            return int(self.get_element_text(self.COMPLETED_FOR_ALL_TIME_COUNTER, timeout))

        @allure.step('Проверить, что заказов в работе нет')
        def check_empty_orders_in_work(self, timeout=5):
            return self.wait_until_visible(self.NO_ORDERS_MESSAGE, timeout)

        @allure.step('Получить номер заказа из модального окна')
        def check_number_of_order(self, timeout=5):
            return self.wait_until_visible(self.ORDER_NUMBER_MODAL, timeout).text.strip()

        @allure.step('Получить номер заказа из ленты заказов')
        def check_number_of_order_order_feed(self, timeout=5):
            return self.wait_until_visible(self.WORKING_ORDER, timeout).text.strip()

        @allure.step('Получить номер последнего заказа')
        def get_last_order_number(self):
            return self.get_element_text(self.LAST_ORDER_NUMBER_LOCATOR)

        @allure.step('Получить номер заказа из ленты')
        def get_order_number_from_feed(self, timeout=5):
            order_elements = self.find_elements(self.NUMBER_OF_ORDER, timeout)
            first_order_number_feed = order_elements[0].text.strip()
            return first_order_number_feed.lstrip('#')
