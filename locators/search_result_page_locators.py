from selenium.webdriver.common.by import By


class SearchResultsPageLocators(object):
    PRICE_MIN_INPUT = (By.ID, "priceMin")
    PRICE_MAX_INPUT = (By.ID, "priceMax")
    AREA_MIN_INPUT = (By.ID, "areaMin")
    AREA_MAX_INPUT = (By.ID, "areaMax")
    LOCATION_INPUT = (By.XPATH, "//*[@id='location']/div[2]")
