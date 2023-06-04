import time

import allure

from generator.generator import get_city, get_correct_city_name
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

    @allure.step("Checking search city placeholder")
    def check_search_city_input_placeholder(self):
        """Checkin search city placeholder"""
        expected_placeholder = dp.get("search_city_placeholder")
        actual_placeholder = self.element_is_visible(self.locators.SEARCH_CITY_INPUT).get_attribute("placeholder")
        assert actual_placeholder == expected_placeholder, \
            f"Expected placeholder is not equal {expected_placeholder}"

    @allure.step("Checking entered text")
    def check_entered_text(self):
        """Checking entered text"""
        city = next(get_city())
        expected_text = get_correct_city_name(city.city)
        input_field = self.element_is_visible(self.locators.SEARCH_CITY_INPUT)
        input_field.clear()
        input_field.send_keys(expected_text)
        entered_text = input_field.get_attribute("value")
        assert expected_text == entered_text, \
            f"Entered text is not equal {expected_text} or is not displayed"

