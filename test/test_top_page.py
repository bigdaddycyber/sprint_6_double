import allure
from pages.top_page import TopPage
from pages.main_page import MainPage



class TestTopPage:

    @allure.title("Клик по логу Самокат")
    @allure.description("Проверка, что клик по логотипу 'Самокат' переводит на главную страницу")
    def test_click_logo_scooter_follow_link_main(self, browser):
        header_page = TopPage(browser)
        header_page.click_to_order_button_header()
        header_page.click_to_logo_scooter()
        assert header_page.check_main_page()

    @allure.title("Клик по логу Яндекса")
    @allure.description("Проверка, что клик по логу 'Яндекс' переходит на страницу Дзен")
    def test_click_logo_ya_redirect_dzen(self, browser):
        header_page = TopPage(browser)
        header_page.click_to_logo_ya()
        assert header_page.check_redirect_dzen