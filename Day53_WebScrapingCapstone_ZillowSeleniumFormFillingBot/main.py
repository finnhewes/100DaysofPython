import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

CHROME_DRIVER_PATH = '/Users/finnhewes/Developing/chromedriver'
s = Service(CHROME_DRIVER_PATH)
browser = webdriver.Chrome(service=s)
zillow_url = 'https://www.zillow.com/los-angeles-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Los%20Angeles%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-118.668176%2C%22east%22%3A-118.155289%2C%22south%22%3A33.703652%2C%22north%22%3A34.337306%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12447%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2000%7D%2C%22price%22%3A%7B%22max%22%3A471646%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%7D'
google_form_url = 'https://forms.gle/EC1PHKtN1cwR9vf76'

###############################################################################################
# This is the zillow search part of our program. I'm adding everything to an indexed list, so that the
# position/index of the price in the list is the same index as the address and listing link in those
# respective lists, which will allow me to keep track of the data very easily. I could also do this with
# a dictionary, but I chose to do it this way for now!

browser.get(zillow_url)     # go to zillow search
element = WebDriverWait(browser, 10).until(                             # 10 sec MAX pause to let things load.
    EC.presence_of_element_located((By.CLASS_NAME, "list-card-link")))  # Otherwise, an error is thrown..

    # finding listings, getting their links
listings = browser.find_elements(By.CLASS_NAME, "list-card-link")   # this returns a selenium object
listing_links=[]    # adding links to indexed list
for each in listings:
    listing_links.append(each.get_attribute("href"))    # this 'digs' into the selenium object, and returns its href
# using list comprehension to remove duplicates from list
links_list_duplicates_removed = []
[links_list_duplicates_removed.append(link) for link in listing_links if link not in links_list_duplicates_removed]

    # finding prices of all of our listings
price_objs = browser.find_elements(By.CLASS_NAME, "list-card-price") # this returns a selenium object
prices = []     # adding prices to indexed list
for each in price_objs:
    prices.append(each.text) # this 'digs' into the selenium object, and returns its text (the listings price)
# stripping the 'fluff' on the prices... (removing commas and "/mo")
prices_stripped=[]
for each in prices:
    temp_list = each.split("/")
    prices_stripped.append(temp_list[0].replace(",", ""))

    # finding addresses of all of our listings
address_objs = browser.find_elements(By.CLASS_NAME, "list-card-addr") # this returns a selenium object
addresses = []  # adding addresses to an indexed list
for each in address_objs:
    addresses.append(each.text) # this 'digs' into the selenium object, and returns its text (the listings address)

###############################################################################################
# now, we'll add each of these to our Google form, and submit it!

for each in range(0, len(addresses)):
    browser.get(google_form_url)    # rather than clicking the "fill another form" button after the form is submitted,
                                    # I'm just going to start each loop with a fresh url retrieval.
    time.sleep(3)
        # locating elements (inputs and buttons)
    inputs = browser.find_elements(By.CSS_SELECTOR, 'input')
    address_input = inputs[3]
    rent_price_input = inputs[4]
    listing_link_input = inputs[5]
    submit_button = browser.find_element(By.CSS_SELECTOR, 'div > span > span')
        # filling inputs
    address_input.click()   # first, click to activate
    address_input.send_keys(addresses[each])    # then, send keys from lists above
    rent_price_input.click()
    rent_price_input.send_keys(prices_stripped[each])
    listing_link_input.click()
    listing_link_input.send_keys(links_list_duplicates_removed[each])
        # clicking buttons
    submit_button.click()   # send it!

browser.quit()  # close all browser tabs, quit chrome
