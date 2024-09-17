#This file will include a class with instance methods.
#That will be responsible to interact with our website.
#After we have some results, apply filters.
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver #This ensures we declare a type for the self.driver object hence can allow auto-completions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver


    def apply_star_rating(self, *filters):
        popular_filtration_box = self.driver.find_element(
            By.ID, "filter_group_popular_:rm:"
        )
        popular_child_elements = popular_filtration_box.find_elements(
            By.CSS_SELECTOR, "div[data-filters-item]"
        )
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "filter_group_popular_:rm:"))
        )

        for filter_item in filters:
            for element in popular_child_elements:
                innerHTML = str(element.get_attribute("innerHTML")).strip()
                if f"{filter_item}" in innerHTML:
                    element.click()

    def sort_price_lowest(self):
        drop_down_sorters = self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='sorters-dropdown-trigger']")

        drop_down_sorters.click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-id="price"]'))
        )
        lowest_price = self.driver.find_element(By.CSS_SELECTOR, 'button[data-id="price"]')
        lowest_price.click()


