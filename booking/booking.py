import time

from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.expected_conditions import element_to_be_selected
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException, TimeoutException


import booking.constants as const
from selenium import webdriver
from booking.booking_filtrations import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable

class Booking:
    def __init__(self, driver: webdriver):
        #Initialize the Chrome driver
        self.driver = driver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
            self.driver.quit()

    def land_first_page(self):
        self.driver.get(const.BASE_URL)

    # def close_any_popups(self):
    #
    #     try:
    #         wait = WebDriverWait(self.driver, 10)
    #         close_signin_popup = wait.until(
    #             EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Dismiss sign-in info.']")))
    #         close_signin_popup.click()
    #         print('Pop up closed')
    #
    #
    #     except:
    #         pass

    def close_any_popups(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            close_signin_popup = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Dismiss sign-in info.']"))
            )
            close_signin_popup.click()
            print('Pop up closed')

        except (TimeoutException, NoSuchElementException) as e:
            print(f"No pop-up found or an error occurred: {e}")

    #
    #     try:
    #         accept_cookies_button = self.driver.find_element(By.XPATH, "//button[text()='Accept']")
    #         accept_cookies_button.click()
    #         print('Cookies accepted')
    #         #pop_up_closed = True
    #     except:
    #         pass


    def change_currency(self, currency=None):
        wait = WebDriverWait(self.driver, 10)

        #Find currency menu
        time.sleep(2)
        currency_element = self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='header-currency-picker-trigger']")
        self.driver.execute_script("arguments[0].click();", currency_element)

        # Wait for the currency options to be visible | Note we're using find_elements(s) not just element
        selected_currency = wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "button[data-testid='selection-item'][class='a83ed08757 aee4999c52 ffc914f84a c39dd9701b ac7953442b']")))

        # Click the desired currency option (U.S. Dollar) | From the list of elements
        for element in selected_currency:
            try:
                if 'USD' in element.text:
                    time.sleep(3)
                    element.click()
                    break
            except NoSuchElementException:
                pass


    def which_country(self, place_to_go):
        # self.close_any_popups()

        wait = WebDriverWait(self.driver, 15)

        # Retry loop for handling stale element reference
        for _ in range(3):
            try:
                search_field = wait.until(
                    EC.element_to_be_clickable((By.ID, ':rh:'))
                )
                search_field.send_keys(place_to_go)
                break
            except (ElementNotInteractableException, StaleElementReferenceException, ElementClickInterceptedException):
                self.driver.execute_script("arguments.scrollIntoView(true);", search_field)
        time.sleep(2)

        # Retry loop for handling stale element reference
        for _ in range(3):
            try:
                first_result = wait.until(
                    EC.element_to_be_clickable((By.ID, 'autocomplete-result-0'))
                )
                first_result.click()
                break
            except (ElementNotInteractableException, StaleElementReferenceException, ElementClickInterceptedException):
                self.driver.execute_script("arguments.scrollIntoView();", first_result)

    def select_dates(self, check_in, check_out):
        check_in_element = self.driver.find_element(By.CSS_SELECTOR, f'span[data-date="{check_in}"]')
        check_in_element.click()

        check_out_element = self.driver.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out}"]')
        check_out_element.click()

    def select_adults(self, count=1):
        selection_element = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]')
        selection_element.click()

        while True:
            decrease_adults = self.driver.find_element(By.CLASS_NAME, 'a83ed08757.c21c56c305.f38b6daa18.d691166b09.ab98298258.e91c91fa93')
            decrease_adults.click()

            #If value of adults gets to 1, then break out of the while loop
            adults_value_element = self.driver.find_element(By.ID, 'group_adults')
            adults_value = adults_value_element.get_attribute('value') #This should give out the adults value

            if int(adults_value) == 1:
                break

        increase_adults = self.driver.find_element(By.CLASS_NAME,
                                                   'a83ed08757.c21c56c305.f38b6daa18.d691166b09.ab98298258.bb803d8689.f4d78af12a')

        for i in range(count - 1): #incase the count is 1, for loop cannot have a range of 0 so it's automatically going to pick the 1 guest inputed
            increase_adults.click()

    def click_search(self):
        search_element = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_element.click()

        time.sleep(2)
    def apply_filters(self):
        self.close_any_popups()

        filtration = BookingFiltration(driver=self.driver) #This new class is to prevent the booking file from having too many methods
        #Pass the driver attribute
        filtration.apply_star_rating("Free cancellation", "Very Good: 8+")
        time.sleep(2)
        filtration.sort_price_lowest()

        # time.sleep(3)
    def report_results(self):
        time.sleep(1)
        hotel_boxes = self.driver.find_element(By.CSS_SELECTOR, 'div[class="d4924c9e74"]')
        report = BookingReport(hotel_boxes)
        table = PrettyTable(
            field_names = ["Hotel Name", "Hotel Price", "Hotel Score"]
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)





        # # Close the WebDriver
        #    # self.driver.quit()

