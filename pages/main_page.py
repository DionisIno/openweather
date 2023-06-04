import allure

from generator.generator import get_city
from locators.main_page_locators import MainPageLocators
from data.urls import main_page_urls as urls
from data.test_data_main_page import data_main_page as dp
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    @allure.step("Checking current url")
    def check_main_page_current_url(self):
        """Valid url check"""
        expected_url = urls.get("BASE_URL")
        actual_url = self.driver.current_url
        assert expected_url == actual_url, \
            f"Current url is not equal {expected_url}"

    @allure.step("Checking current title")
    def check_main_page_title(self):
        """Valid title check"""
        expected_title = dp.get("title")
        actual_title = self.driver.title
        assert expected_title == actual_title, \
            f"Actual title is not equal {expected_title}"

    # city = next(get_city())
    # city_name = str(city).split("'")[5]
    # country_name = str(city).split("'")[7]
    # a = ', '.join([city_name, country_name])
    # print(a)
