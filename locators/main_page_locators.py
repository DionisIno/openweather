from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_CITY_INPUT = (By.CSS_SELECTOR, "div[class='search-container'] > input[type=text]")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[class='button-round dark']")
    FIRST_SELECTED_CITY = (By.CSS_SELECTOR, "ul[class='search-dropdown-menu'] li:nth-child(1)")
    DISPLAYED_CITY_H2_HEADER = (By.CSS_SELECTOR, "ul[class='search-dropdown-menu'] li:nth-child(1)")
    MESSAGE = (By.CSS_SELECTOR, "div[class='sub not-found notFoundOpen']")
    NO_RESULT_MESSAGE = (By.CSS_SELECTOR, "div[class='widget-notification']")
