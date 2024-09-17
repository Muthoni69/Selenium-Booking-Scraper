from selenium.webdriver.ie.webdriver import WebDriver

from booking.booking import Booking

with Booking(driver=WebDriver) as bot:

    bot.land_first_page()
    bot.close_any_popups()
    bot.change_currency()
    bot.which_country(input('Where do you wanna go?')) #Input is useful especially when running bot on CLI
    bot.select_dates(check_in=input("What is your check in date in YY-MM-DD?"),
                    check_out=input("What is your check out date in YY-MM-DD?"))
    bot.select_adults(int(input('How many people?')))
    bot.click_search()
    bot.apply_filters()

    bot.report_results()