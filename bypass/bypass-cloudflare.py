from undetected_chromedriver import Chrome
import time

# create a new instance of Chrome
chrome = Chrome()

# navigate to the website
chrome.get("https://example.com")

time.sleep(10)
# close the browser
chrome.close()
