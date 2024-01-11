import time
import json
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.dicts import css_selectors_dict
from utils.helper_functions import get_links_list, get_row_dict, initialize_search

#SEARCH_PHRASE = "flow"
CITY_PHRASE = "Radom"
# Get current time and format it as a string in "year-month-day-hour-minute" format
current_time = datetime.now()
time_string = current_time.strftime("%Y-%m-%d-%H-%M")

# Keep Chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

initialize_search(driver=driver, min=50, max=55, city=CITY_PHRASE)

time.sleep(2) # zmienić na Wait Until Load

# Get hold of a links for the offers
links_list = get_links_list(driver)

data_dict = {}

for link in links_list:
    row_dict, order_num = get_row_dict(driver, links_list, link, CITY_PHRASE, time_string, css_selectors_dict)
    print(row_dict)
    data_dict[order_num] = row_dict
print(data_dict)

# save as json file
file_path = fr"C:\Users\ADMIN\Desktop\Pliki\Data_Stuff\Python\books_scrapper\json_data\{time_string}_{CITY_PHRASE}_output.json"
with open(file_path, 'w', encoding='utf-8') as json_file:
    json.dump(data_dict, json_file, ensure_ascii=False)


