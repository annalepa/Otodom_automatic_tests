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
    ESTATE_TYPE_LIST_BUTTON = (By.XPATH, "//div[@data-cy='search-form--field--estate']//div[@aria-hidden]")
    SEARCH_FROM_LOCATION_LIST = [By.XPATH,
                                 '//*[@id="__next"]/main/section[1]/div/div/form/div/div[1]/div[3]/div/div['
                                 '1]/div/div[2]']


class SearchResultsPageLocators(object):
    PRICE_MIN_INPUT = (By.ID, "priceMin")
    PRICE_MAX_INPUT = (By.ID, "priceMax")
    AREA_MIN_INPUT = (By.ID, "areaMin")
    AREA_MAX_INPUT = (By.ID, "areaMax")
    LOCATION_INPUT = (By.XPATH, "//*[@id='location']/div[2]")
    pass
