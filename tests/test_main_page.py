import allure
from data.urls import main_page_urls as urls

from pages.main_page import MainPage


@allure.epic("Testing Main Page")
class TestMainPage:

    @allure.title("Testing main page current url")
    def test_check_current_url_main_page(self, driver):
        """This test checks the current site url"""
        page = MainPage(driver, urls.get("BASE_URL"))
        page.open()
        page.check_main_page_current_url()

    @allure.title("Testing main page current title")
    def test_check_title_main_page(self, driver):
        """This test checks the actual site title"""
        page = MainPage(driver, urls.get("BASE_URL"))
        page.open()
        page.check_main_page_title()

    @allure.title("Checking search city placeholder")
    def test_city_search_field_placeholder(self, driver):
        """This test checks that the placeholder contains valid text"""
        page = MainPage(driver, urls.get("BASE_URL"))
        page.open()
        page.check_search_city_input_placeholder()

    @allure.title("Checking that the entered text is visible on the screen")
    def test_entered_text_is_displayed(self, driver):
        """This test checks that the entered text is visible on the screen"""
        page = MainPage(driver, urls.get("BASE_URL"))
        page.open()
        page.check_entered_text()
