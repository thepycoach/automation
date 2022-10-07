from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

path = '/Users/frankandrade/Downloads/chromedriver'
service = Service(executable_path=path)
web = 'https://tinder.com/'

mensaje_ligar = "Hola!"
numero_likes = 10

options = Options()
options.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(service=service, options=options)

driver.get(web)

time.sleep(3)
for i in range(numero_likes):
    try:
        time.sleep(3)
        like_button = driver.find_element(by='xpath', value='//button//span[text()="Like"]')
        driver.execute_script("arguments[0].click();", like_button)
        time.sleep(2)

        match_window = driver.find_element(by='xpath', value='//textarea[@placeholder="Say something nice!"]')
        match_window.send_keys(mensaje_ligar)
        time.sleep(1)

        send_message_button = driver.find_element(by='xpath', value='//button/span[text()="Send"]')
        send_message_button.click()
        time.sleep(1)

        close_its_match_window = driver.find_element(by='xpath', value='//button[@title="Back to Tinder"]')
        close_its_match_window.click()

    except:
        try:
            box = driver.find_element(by='xpath', value='//button/span[text()="Maybe Later"] | //button/span[text()="Not interested"] | //button/span[text()="No Thanks"]')
            box.click()
        except:
            pass

