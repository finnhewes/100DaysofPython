This bot takes a Zillow search link, with filters already applied, and a link to a Google form as inputs.

It scrapes Zillow for the listings in the search link, and retrieves the prices, addresses, and links to all listings (on the first page) of the search.
Then, it navigates to the Google form, and fills it out, and submits it. One submission for each listing in the Zillow search.

I got this bot to work, but would have liked to use more 'native' solutions, such as Selenium's built-in wait function, rather than relying on "time.sleep"...
A next iteration to this project could be implementing these native solutions, and possibly finding the number of total listings given the search parameters, and if we've yet to reach the end of the search, page forward and keep scraping.

I tried this bot with a different link for a Zillow search in a different location with different parameters, and the bot was unable to advance past the first 20 or 25 listings, at the end of the first page.
Duh. 

The original project "requirements" from Angela Yu stated that BeautifulSoup was to be used in combination with Selenium, but I was unable to pass captcha with BS4.
Instead of signing up for a Zillow API account, I decided to just scrape all of the data using Selenium.
