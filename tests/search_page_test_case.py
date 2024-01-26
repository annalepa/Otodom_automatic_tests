from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from page.search_result_page import SearchResultPage


class SearchResultPageTestCase(TestCase):
    def setUp(self):
        print("setUp")
        chrome_options = Options()
        # chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.get('https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/cala-polska?viewType=listing')

    def test_more_filters(self):
        search_result_page = SearchResultPage(self.driver)
        search_result_page.click_accept_button()
        search_result_page.click_more_filters()
        search_result_page.click_dropdown_floors()
        search_result_page.click_checkbox_second_floor()

    def tearDown(self):
        self.driver.close()
