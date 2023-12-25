import allure
from locators import MainLocators
from pages.main_page import BigPage



class TopPage(BigPage):

    @allure.step("Кликнуть по кнопке 'Заказать' в заголовке")
    def click_to_order_button_header(self):
        self.click_to_element(MainLocators.ORDER_BUTTON_TOP)

    @allure.step("Кликнуть по логотипу 'Самокат'")
    def click_to_logo_scooter(self):
        self.click_to_element(MainLocators.LOGO_SAMOCAT)

    @allure.step("Проверить, что перешли на главную страницу")
    def check_main_page(self):
        return self.find_definite_element(MainLocators.HEADER_ON_MAIN)

    @allure.step("Кликнуть по логотипу 'Яндекс'")
    def click_to_logo_ya(self):
        self.click_to_element(MainLocators.LOGO_YANDEX)

    @allure.step("Проверить, что открылась новая вкладка Дзен")
    def check_redirect_dzen(self):
        self.redirect_new_tab()
        return self.find_definite_element(MainLocators.DZEN_HEADER)