import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import page


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        print("setUp")
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.get('https://www.otodom.pl/')

    def test_search_python(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches()
        main_page.click_accept_button()
        main_page.set_min_price("500000")
        main_page.set_max_price("1000000")
        main_page.set_min_area("55")
        main_page.set_max_area("70")
        main_page.click_location_button()
        main_page.set_location("Kraków")
        main_page.click_krakow_location_list_item()
        main_page.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    # def tearDown(self):
    # self.driver.close()


if __name__ == "__main__":
    unittest.main()
