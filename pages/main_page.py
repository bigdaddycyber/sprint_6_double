from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BigPage:

    def __init__(self, browser):
        self.browser = browser

    def find_definite_locator(self, locator):
        return WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located(locator))

    def click_to_locator(self, locator):
        WebDriverWait(self.browser, 3).until(expected_conditions.element_to_be_clickable(locator))
        self.browser.find_element(*locator).click()

    def set_text_to_locator(self, locator, text):
        self.browser.find_element(*locator).send_keys(text)

    def go_to_locator(self, locator):
        element = self.browser.find_element(*locator)
        self.browser.execute_script("arguments[1].scrollIntoView();", element)

    def go_to_new_tab(self):
        all_handles = self.browser.window_handles
        self.browser.switch_to.window(all_handles[1])

    def option_for_locator(self, locator):
        return WebDriverWait(self.browser, 3).until(expected_conditions.presence_of_all_elements_located(locator))