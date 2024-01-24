import self
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.search_result_page_locators import SearchResultsPageLocators


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