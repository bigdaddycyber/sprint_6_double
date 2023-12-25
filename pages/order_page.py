import random
import allure
from locators import MainLocators
from pages.main_page import BigPage


class OrderPage(BigPage):

    @allure.step("Кликнуть по кнопке 'Заказать' вверху страницы")
    def click_to_order_button_header(self):
        self.click_to_element(MainLocators.ORDER_BUTTON_ON_TOP)

    @allure.step("Проскролить до кнопки 'Заказать' внизу страницы")
    def scroll_to_order_button_down(self):
        self.scroll_to_element(MainLocators.ORDER_BUTTON_ON_DOWN)
        return self.find_definite_element(MainLocators.ORDER_BUTTON_ON_DOWN)

    @allure.step("Кликнуть по кнопке 'Заказать' внизу страницы")
    def click_to_order_button_down(self):
        self.click_to_element(MainLocators.ORDER_BUTTON_ON_DOWN)

    @allure.step("Кликнуть по кнопке 'да все привыкли'")
    def click_to_cookie_button(self):
        self.click_to_element(MainLocators.COOKIE_APPLY)

    @allure.step("Данные для поля 'Имя'")
    def set_name_to_field(self, text):
        self.set_text_to_element(MainLocators.NAME, text)

    @allure.step("Данные для поля 'Фамилия'")
    def set_lastname_to_field(self, text):
        self.set_text_to_element(MainLocators.LASTNAME, text)

    @allure.step("Данные для поля 'Адрес'")
    def set_address_to_field(self, text):
        self.set_text_to_element(MainLocators.ADDRESS, text)

    @allure.step("Данные для поля 'Метро'")
    def click_to_metro(self):
        self.click_to_element(MainLocators.METRO)

    @allure.step("Выбрать станцию метро из выпадающего списка")
    def choose_metro_station(self):
        method, locator = MainLocators.CHOOSE_METRO
        number = random.randint(1, 112)
        locator = locator.format(num=number)
        self.click_to_element((method, locator))

    @allure.step("Данные для поля 'Телефон'")
    def set_phone_to_field(self, text):
        self.set_text_to_element(MainLocators.PHONE, text)

    @allure.step("Кликнуть по кнопке 'Далее'")
    def click_to_onward_button(self):
        self.click_to_element(MainLocators.ONWARD_BUTTON)

    @allure.step("Данные для поля 'Когда привезти самокат'")
    def set_date_to_field(self, text):
        self.set_text_to_element(MainLocators.WHEN_BACK, text)

    @allure.step("Выбрать дату в календаре")
    def click_to_choose_date(self):
        self.click_to_element(MainLocators.CHOOSE_DATE)

    @allure.step("Кликнуть по полю 'Срок аренды'")
    def click_to_rent_date(self):
        self.click_to_element(MainLocators.LIMIT)

    @allure.step("Выбрать 'Срок аренды' из выпадающего списка")
    def choose_date(self):
        options = self.find_option_elements(MainLocators.CHOOSE_LIMIT)
        random_option = random.choice(options)
        random_option.click()

    @allure.step("Выбрать любой самокат")
    def choose_scooter(self):
        options = self.find_option_elements(MainLocators.CHOOSE_SAMOCAT)
        random_option = random.choice(options)
        random_option.click()

    @allure.step("Комментарий для курьера")
    def set_comment_to_field(self, text):
        self.set_text_to_element(MainLocators.COMMENT, text)

    @allure.step("Кликнуть по кнопке заказа")
    def click_to_order_button(self):
        self.click_to_element(MainLocators.BUTTON_ORDER)

    @allure.step("Подтвердить заказ")
    def click_to_confirm_button(self):
        self.click_to_element(MainLocators.YES_BUTTON)

    @allure.step("Проверить, что заказ успешный")
    def check_success_order(self):
        return self.find_definite_element(MainLocators.STATUS_BUTTON)

    @allure.step("Кнопку 'Посмотреть статус'")
    def click_to_status_button(self):
        self.click_to_element(MainLocators.STATUS_BUTTON)

    @allure.step("Проверить, что перешли на страницу заказа")
    def check_order_page(self):
        return self.find_definite_element(MainLocators.CANCEL_BUTTON)

    def create_order(self, name, lastname, address, phone, date, comment):
        self.set_name_to_field(name)
        self.set_lastname_to_field(lastname)
        self.set_address_to_field(address)
        self.click_to_metro()
        self.choose_metro_station()
        self.set_phone_to_field(phone)
        self.click_to_onward_button()
        self.set_date_to_field(date)
        self.click_to_choose_date()
        self.click_to_rent_date()
        self.choose_date()
        self.choose_scooter()
        self.set_comment_to_field(comment)
        self.click_to_order_button()
        self.click_to_confirm_button()
        self.check_success_order()
        self.click_to_status_button()