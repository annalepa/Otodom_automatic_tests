from selenium.webdriver.common.by import By


class MainPageLocators(object):
    SEARCH_BUTTON = (By.ID, "search-form-submit")
    PRICE_MIN_INPUT = (By.ID, "priceMin")
    PRICE_MAX_INPUT = (By.ID, "priceMax")
    ACCEPT_BUTTON = (By.ID, "onetrust-accept-btn-handler")


class SearchResultsPageLocators(object):
    pass
