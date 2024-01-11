import time
import json
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.dicts import css_selectors_dict
from utils.helper_functions import get_links_list, get_row_dict

#SEARCH_PHRASE = "flow"
CITY_PHRASE = "Plock"
# Get current time and format it as a string in "year-month-day-hour-minute" format
current_time = datetime.now()
time_string = current_time.strftime("%Y-%m-%d-%H-%M")

# Keep Chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.otodom.pl/")

time.sleep(1)
cookies_button = driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
cookies_button.click()


min_pow = driver.find_element(By.ID, value="areaMin")
min_pow.send_keys("30")
max_pow = driver.find_element(By.ID, value="areaMax")
max_pow.send_keys("100")

spot = driver.find_element(By.CLASS_NAME, value="css-1171ahe")
spot.click()
search_bar = driver.find_element(By.XPATH, value='//*[@id="location-picker-input"]')
search_bar.send_keys(CITY_PHRASE)
time.sleep(1)
checkbox = driver.find_element(By.CLASS_NAME, value="css-104jm27")
checkbox.click()
time.sleep(1)
search_button = driver.find_element(By.ID, value="search-form-submit")
search_button.click()

time.sleep(2) # zmienić na Wait Until Load
# linki do ofert

#link_elements_list = driver.find_elements(By.CLASS_NAME, value="css-lsw81o")
#links_list = []
links_list = get_links_list(driver)



data_dict = {}

# for element in link_elements_list:
#     links_list.append(element.get_attribute("href"))
#     print(element.get_attribute("href"))

#row_dict = {}

for link in links_list:
    row_dict, order_num = get_row_dict(driver, links_list, link, CITY_PHRASE, time_string, css_selectors_dict)
    # row_dict = {}
    # order_num = links_list.index(link)
    #
    # driver.get(link)
    # time.sleep(1)
    #
    # row_dict["link"] = link
    # row_dict["city"] = CITY_PHRASE
    # try:
    #     row_dict["title"] = driver.find_element(By.XPATH, value='//*[@id="__next"]/main/div[2]/div[2]/header/h1').text
    # except:
    #     row_dict["title"] = None
    #
    # try:
    #     row_dict["price"] = driver.find_element(By.CLASS_NAME, value="css-t3wmkv").text
    # except:
    #     row_dict["price"] = None
    #
    # try:
    #     row_dict["price_sqm"] = driver.find_element(By.CLASS_NAME, value='css-1h1l5lm').text
    # except:
    #     row_dict["price_sqm"] = None
    #
    # try:
    #     row_dict["when_added_approx_days"] = driver. find_element(By.CLASS_NAME, value="css-1soi3e7").text
    # except:
    #     row_dict["when_added_approx_days"] = None
    #
    # row_dict["scrap_time"] = time_string
    #
    # for key, value in css_selectors_dict.items():
    #     try:
    #         row_dict[key] = driver.find_element(By.CSS_SELECTOR, value=value).text
    #     except:
    #         row_dict[key] = None
    print(row_dict)
    data_dict[order_num] = row_dict
print(data_dict)

# save as json file
file_path = fr"C:\Users\ADMIN\Desktop\Pliki\Data_Stuff\Python\books_scrapper\json_data\{time_string}_{CITY_PHRASE}_output.json"
with open(file_path, 'w', encoding='utf-8') as json_file:
    json.dump(data_dict, json_file, ensure_ascii=False)



    #break


