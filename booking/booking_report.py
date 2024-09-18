#This file is going to include method that will parse
#The specific data that we need from each one of the deal boxes

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BookingReport:
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(By.CSS_SELECTOR, "div[data-testid='property-card']")

    def pull_deal_box_attributes(self):
        wait = WebDriverWait(self.boxes_section_element, 10)
        collection = []
        for deal_box in self.deal_boxes:
            # Titles
            hotel_name = deal_box.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').get_attribute(
                'innerHTML').strip()
            # print(hotel_name)

            # Prices
            hotel_price = deal_box.find_element(By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]').get_attribute(
                'innerHTML').strip()
            # print(hotel_price)

            # Rating
            hotel_score = WebDriverWait(self.boxes_section_element, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="review-score"]'))
            ).find_element(By.CSS_SELECTOR, 'div[class="ac4a7896c7"]').text

            # hotel_score = WebDriverWait(self.boxes_section_element, 10).until(
            #     EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="review-score"]'))).find_element(
            #     By.CSS_SELECTOR, 'div[class="ac4a7896c7"]').text

            # print(hotel_score)

            collection.append([hotel_name, hotel_price, hotel_score])
        return collection

