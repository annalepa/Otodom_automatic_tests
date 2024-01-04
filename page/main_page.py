from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators
from page.base_page import BasePage


class MainPage(BasePage):

    def is_title_matches(self) -> bool:
        return "Otodom" in self.driver.title

    def click_search_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.SEARCH_BUTTON)
        )
        element.click()

    def click_accept_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ACCEPT_BUTTON)
        )
        element.click()

    def set_min_price(self, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.PRICE_MIN_INPUT)
        )
        element.clear()
        element.send_keys(value)

    def set_max_price(self, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.PRICE_MAX_INPUT)
        )
        element.clear()
        element.send_keys(value)

    def set_min_area(self, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.AREA_MIN_INPUT)
        )
        element.clear()
        element.send_keys(value)

    def set_max_area(self, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.AREA_MAX_INPUT)
        )
        element.clear()
        element.send_keys(value)

    def click_location_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.SEARCH_LOCATION_BUTTON)
        )
        element.click()

    def set_location(self, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.LOCATION_INPUT)
        )
        element.clear()
        element.send_keys(value)

    def click_krakow_location_list_item(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.KRAKOW_LOCATION_LIST_ITEM)
        )
        element.click()

    def click_estate_type_list(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ESTATE_TYPE_LIST_BUTTON)
        )
        element.click()

    def search_from_location_list_is_displayed(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.SEARCH_FROM_LOCATION_LIST)
        )
        return element.is_displayed()
