from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
##############################################################################

s=Service("/Users/finnhewes/Developing/chromedriver")
browser = webdriver.Chrome(service=s)

# url to be accessed
url = "https://www.youtube.com/"

browser.get(url)

logo = browser.find_element(By.ID, "logo-icon")
searchbar = browser.find_element(By.NAME, "search_query")
first_video_title = browser.find_element(By.CSS_SELECTOR, "#video-title.style-scope.ytd-rich-grid-media").text
video_titles = browser.find_elements(By.CSS_SELECTOR, "#video-title.style-scope.ytd-rich-grid-media")
signin_text = browser.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/tp-yt-paper-button/yt-formatted-string").text
print(logo)
print(type(searchbar))
print(first_video_title)
for each in video_titles:
    print(each.text)
print(signin_text)

browser.quit()
