from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.maximize_window()
driver.get('https://store.hermanmiller.com/')

python_button = driver.find_element_by_xpath("/html/body/div[1]/header/nav/div/div/div[2]/div[2]/a")
python_button.click()
search = driver.find_element_by_name("q")
search.send_keys("Aeron")
search.send_keys(Keys.RETURN)

time.sleep(3)
product_button = driver.find_element_by_xpath('//*[@id="product-search-results"]/div[2]/div/div[2]/div[2]/div[1]')
product_button.click()
time.sleep(1)
print(driver.current_url)

