from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def find_and_click(self, locator, index=0):
        elements = self.find_elements(locator)
        element = elements[index]
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(EC.element_to_be_clickable(element))
        element.click()

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def wait_until_visible(self, locator, timeout=60):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click_and_wait(self, locator, next_locator):
        self.click_element(locator)
        self.wait_until_visible(next_locator)

    def scroll_and_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_new_tab(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])

    def wait_for_url(self, expected_url):
        self.wait.until(EC.url_to_be(expected_url))


    def click_all_and_close_modal(self, elements_locator, modal_locator, close_button_locator):
        elements = self.find_elements(elements_locator)
        for index in range(len(elements)):
            elements = self.find_elements(elements_locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", elements[index])
            elements[index].click()

            self.wait.until(EC.visibility_of_element_located(modal_locator))
            self.find_element(close_button_locator)

            self.wait.until(EC.invisibility_of_element_located(modal_locator))

    def drag_and_drop(self, source, target):
        actions = ActionChains(self.driver)
        actions.click_and_hold(source).move_to_element(target).release().perform()

    def get_element_text(self, locator, timeout=5):
        element = self.wait_until_visible(locator, timeout)
        return element.text

    def scroll_and_get_last_element_text(self, elements_locator, text_locator, timeout=5):
        elements = self.find_elements(elements_locator, timeout)

        for element in elements:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)

        last_element = elements[-1]
        text_element = last_element.find_element(*text_locator)

        return text_element.text.strip()