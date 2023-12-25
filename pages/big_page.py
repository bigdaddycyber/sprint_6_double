import allure
from locators import MainLocators
from pages.main_page import BigPage



class MainPage(BigPage):

    @allure.step("Кликнуть 'да все привыкли'")
    def click_to_cookie_button(self):
        self.click_to_element(MainLocators.COOKIE_APPLY)

    @allure.step("Перейти в блок 'Вопросы о важном'")
    def scroll_to_questions(self):
        self.scroll_to_element(MainLocators.IMPORTANT_QUESTIONS)
        return self.find_definite_element(MainLocators.IMPORTANT_QUESTIONS)

    @allure.step("Кликнуть по вопросу")
    def get_question(self, num):
        method, locator = MainLocators.QUESTION
        locator = locator.format(num)
        self.click_to_element((method, locator))
        return self.find_definite_element((method, locator))

    @allure.step("Разница ответов")
    def get_answer(self, num):
        method, locator = MainLocators.ANSWER
        locator = locator.format(num)
        return self.find_definite_element((method, locator)).text