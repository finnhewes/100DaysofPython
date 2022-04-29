from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

###############################################################################################
username = YOUR_USERNAME
password = YOUR_PASSWORD
phone = YOUR_PHONE_NUMBER
###############################################################################################

s=Service(YOUR_WEB_DRIVER_PATH)
browser = webdriver.Chrome(service=s)
url = LINKEDIN_URL_WITH_YOUR_SEARCH_PARAMETERS
browser.get(url)

sign_in_button = browser.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(.5)
username_input = browser.find_element(By.CSS_SELECTOR, "#username")
username_input.send_keys(username)
password_input = browser.find_element(By.CSS_SELECTOR, "#password")
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)
hide_messages_button = browser.find_element(By.XPATH, "/html/body/div[6]/aside/div[1]/header/div[3]/button[2]")
hide_messages_button.click()

job_listings = browser.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")
for listing in job_listings:
    listing.click()
    time.sleep(1)
    end_of_listing = False
    while not end_of_listing:
        try:
            easy_apply_button = browser.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[2]/div[3]/div/div/div/button")
            easy_apply_button.click()    # click easy apply
            try:
                browser.find_element(By.LINK_TEXT, "Submit Application").click()    # try to click submit
            except NoSuchElementException:  # submit option not yet available
                try:
                    browser.find_element(By.LINK_TEXT, "Review").click()    # try to click review
                except NoSuchElementException:  # review option not yet available
                    try:
                        browser.find_element(By.LINK_TEXT, "Next").click()    # try to click next
                        time.sleep(.5)
                        # Here, I'm catching any error messages caused by trying to progress through a form without
                        # entering required information.
                        try:
                            driver.find_elements_by_xpath("(//*[contains(text(), '" + 'Please enter a valid answer' +
                                                          "')] | //*[@value='" + 'Please enter a valid answer' + "'])")
                            # if we find an element with this error message, we'll exit the window and discard our application
                            browser.find_element(By.XPATH,
                                                 "/html/body/div[3]/div/div/button").click()  # exits popup window
                            time.sleep(.5)
                            discard_button = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[3]/button[1]")
                            discard_button.click()  # clicks discard
                        except NoSuchElementException:
                            pass    # PASSES if no error messages come up
                    except NoSuchElementException:      # if there is no option for next, we'll exit the window
                        browser.find_element(By.XPATH, "/html/body/div[3]/div/div/button").click() # exits popup window
                        time.sleep(.5)
                        discard_button = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[3]/button[1]")
                        discard_button.click()  # clicks discard
                    # finally:
                    #     end_of_listing = Trues
            finally:
                end_of_listing = True
        except NoSuchElementException: #  no easy apply, or already applied to this listing
            break
