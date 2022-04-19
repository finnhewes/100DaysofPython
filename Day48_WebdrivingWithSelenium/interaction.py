from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

###############################################################################################

s=Service("/Users/finnhewes/Developing/chromedriver")
browser = webdriver.Chrome(service=s)

###############################################################################################

# Part one, learn to interact with a site, like wikipedia.

        # url="https://en.wikipedia.org/wiki/Main_Page"
        # browser.get(url)
            # find article numbers
        # art_anchor = browser.find_element(By.CSS_SELECTOR, "#articlecount a")
        # art_number=art_anchor.text
        # print(art_number)
            # search a term.
        # search = browser.find_element(By.NAME, "search")
        # search.send_keys("Python")
        # search.send_keys(Keys.ENTER)
        # browser.close()

###############################################################################################

# Part Two, interact with a form,

input_url = "https://secure-retreat-92358.herokuapp.com/"
browser.get(input_url)
first_name_input = browser.find_element(By.NAME, "fName")
first_name_input.send_keys("Finn")
last_name_input = browser.find_element(By.NAME, "lName")
last_name_input.send_keys("Hewes")
email_input = browser.find_element(By.NAME, "email")
email_input.send_keys("finnhewes@gmail.com")
# submit data
submit_button = browser.find_element(By.CSS_SELECTOR, "form button")
submit_button.click()
