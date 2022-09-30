from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

path = '/Users/frankandrade/Downloads/chromedriver'  # your path goes here
service = Service(executable_path=path)
website = 'https://forms.gle/YuQczM1pVUxnkuWL9'  # your own form goes here
driver = webdriver.Chrome(service=service)

df = pd.read_csv('fake_data.csv')

for i in range(0, len(df)):
    driver.get(website)
    time.sleep(3)
    for column in df.columns:
        text_input = driver.find_element(by='xpath', value=f'//div[contains(@data-params, "{column}")]//input | '
                                                           f'//div[contains(@data-params, "{column}")]//textarea')
        text_input.send_keys(df.loc[i, column])
    submit_button = driver.find_element(by='xpath', value='//div[@role="button"]//span[text()="Submit"]')
    submit_button.click()

driver.quit()



