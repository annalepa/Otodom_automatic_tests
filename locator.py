from selenium.webdriver.common.by import By


class MainPageLocators(object):
    SEARCH_BUTTON = (By.ID, "search-form-submit")
    PRICE_MIN_INPUT = (By.ID, "priceMin")
    PRICE_MAX_INPUT = (By.ID, "priceMax")
    ACCEPT_BUTTON = (By.ID, "onetrust-accept-btn-handler")
    AREA_MIN_INPUT = (By.ID, "areaMin")
    AREA_MAX_INPUT = (By.ID, "areaMax")
    SEARCH_LOCATION_BUTTON = (By.ID, "location")
    LOCATION_INPUT = (By.ID, "location-picker-input")
    KRAKOW_LOCATION_LIST_ITEM = (By.XPATH, "//li[starts-with(@data-testid, 'suggestions-item')]")


class SearchResultsPageLocators(object):
    pass
