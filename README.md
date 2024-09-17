# Selenium Booking Scraper

A simple yet powerful web scraping tool built with Selenium, designed specifically to extract hotel data from Booking.com.

## Features

- **User-friendly:** Easy to use with guided prompts for input.
- **Customizable:** Change currency, search location, check-in/out dates, and number of guests.
- **Filtered Results:** Apply filters to refine your hotel search.
- **Detailed Reports:** Get a clear report of hotel names, prices, and ratings.
- **Error Handling:** Includes troubleshooting for common Selenium setup issues.

## Requirements

- **Python 3.x:** Make sure you have Python 3 installed.
- **Selenium:** Install Selenium using `pip install selenium`.
- **Web Driver:**
    - Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome) and add its location to your system's PATH.
    - Alternatively, specify the WebDriver path directly in your code.

## Installation

1. **Clone this repository:**
   ```bash
    git clone [https://github.com/AbdulrahmanBaiasy/selenium-booking-scraper]
    cd selenium-booking-scraper
   ```
2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the script**

    ```bash 
    python main.py
    ``` 

4. **Follow the prompts**
    ```
    Enter the desired currency code (e.g., USD, AUD, AED).
    Specify the destination you want to search for.
    Provide check-in and check-out dates in the format yyyy-mm-dd.
    Indicate the number of adults.
    ```


5. **Get results**

    The script will apply filters, and then generate a report of the matching hotels.

