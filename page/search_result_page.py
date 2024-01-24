from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.search_result_page_locators import SearchResultsPageLocators
from page.base_page import BasePage


class SearchResultPage(BasePage):
    def is_results_found(self):
        return "No results found" not in self.driver.page_source

    def get_min_price(self) -> str:
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SearchResultsPageLocators.PRICE_MIN_INPUT)
        )
        return element.get_attribute('value')

    def get_max_price(self) -> str:
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SearchResultsPageLocators.PRICE_MAX_INPUT)
        )
        return element.get_attribute('value')

    def get_min_area(self) -> str:
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SearchResultsPageLocators.AREA_MIN_INPUT)
        )
        return element.get_attribute('value')

    def get_max_area(self) -> str:
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SearchResultsPageLocators.AREA_MAX_INPUT)
        )
        return element.get_attribute('value')

    def get_location(self) -> str:
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SearchResultsPageLocators.LOCATION_INPUT)
        )
        return element.text

    def click_three_rooms(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SearchResultsPageLocators.THREE_ROOMS_CLICK)
        )
        return element.click()

    def click_four_rooms(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SearchResultsPageLocators.FOUR_ROOMS_CLICK)
        )
        return element.click()

    def click_accept_button(self):
        element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(SearchResultsPageLocators.ACCEPT_BUTTON_CLICK)
            )
        return element.click()

    def click_more_filters(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SearchResultsPageLocators.MORE_FILTERS_CLICK)
        )
        return element.click()

