import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By

#SEARCH_PHRASE = "flow"
CITY_PHRASE = "targowek"
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
max_pow.send_keys("45")

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

# Inicjowanie listy wszystkich linków
links_list = []

is_there_next_page = True
while is_there_next_page:
    try:
        link_elements_list = driver.find_elements(By.CLASS_NAME, value="css-lsw81o")
        for element in link_elements_list:
            links_list.append(element.get_attribute("href"))
            #print(element.get_attribute("href"))
        print(len(links_list))

        # Find next page button and check if it is enabled
        next_page_button = driver.find_element(By.CSS_SELECTOR, value='button[data-cy="pagination.next-page"]')
        if not next_page_button.is_enabled():
            print("No more pages")
            is_there_next_page = False
            break
        next_page_button.click()
        time.sleep(2)
    except:
        print("No more pages")
        is_there_next_page = False

print(links_list)
print(len(links_list))
# linki do ofert oferty
# is_there_next_page = True
# links_list = []
# while is_there_next_page:
#     link_elements_list = driver.find_elements(By.CLASS_NAME, value="css-lsw81o")
#     for element in link_elements_list:
#         links_list.append(element.get_attribute("href"))
#         print(element.get_attribute("href"))
#     try:
#         #next_page_button = driver.find_element(By.CLASS_NAME, value="eo9qioj2")
#         next_page_button = driver.find_element(By.CSS_SELECTOR, value='li[title="Go to next Page"]')
#         aria_disabled_value = element.get_attribute("aria-disabled")
#         if aria_disabled_value == "false":
#             next_page_button.click()
#             time.sleep(1)
#             print("next_page_button found")
#     except:
#         print("next page not found")
#         is_there_next_page = False
#
# print(links_list)
# print(len(links_list))