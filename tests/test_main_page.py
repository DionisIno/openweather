import allure
from data.urls import main_page_urls as urls

from pages.main_page import MainPage


@allure.epic("Testing Main Page")
class TestMainPage:

    @allure.title("Testing main page current url")
    def test_check_current_url_main_page(self, driver):
        """This test checks the current site url"""
        page = MainPage(driver, urls["BASE_URL"])
        page.open()
        page.check_main_page_current_url()

    @allure.title("Testing main page current title")
    def test_check_title_main_page(self, driver):
        """This test checks the actual site title"""
        page = MainPage(driver, urls["BASE_URL"])
        page.open()
        page.check_main_page_title()