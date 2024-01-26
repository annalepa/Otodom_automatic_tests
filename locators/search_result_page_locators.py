from selenium.webdriver.common.by import By


class SearchResultsPageLocators(object):
    PRICE_MIN_INPUT = (By.ID, "priceMin")
    PRICE_MAX_INPUT = (By.ID, "priceMax")
    AREA_MIN_INPUT = (By.ID, "areaMin")
    AREA_MAX_INPUT = (By.ID, "areaMax")
    LOCATION_INPUT = (By.XPATH, "//*[@id='location']/div[2]")
    THREE_ROOMS_CLICK = (By.XPATH, "//*[@id='roomsNumber']/div[4]/label[1]")
    FOUR_ROOMS_CLICK = (By.XPATH, "//*[@id='roomsNumber']/div[5]/label[1]")
    ACCEPT_BUTTON_CLICK = (By.XPATH, "//*[@id='onetrust-accept-btn-handler']")
    MORE_FILTERS_CLICK = (By.XPATH, "//*[@id='__next']/div[2]/main/div[2]/div[1]/div/form/div[3]/div/button["
                                    "2]/span/span[2]")
    DROPDOWN_FLOORS_CLICK = (By.XPATH, "//*[@id='floors']")
    CHECKBOX_SECOND_FLOOR_CLICK = (By.XPATH, "//*[@id='dropdown-checkbox-floors-SECOND']")

