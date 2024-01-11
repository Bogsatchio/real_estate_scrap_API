import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SEARCH_PHRASE = "flow"
CITY_PHRASE = "Plock"

# Keep Chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.otodom.pl/")

time.sleep(1)
cookies_button = driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
cookies_button.click()


min_pow = driver.find_element(By.ID, value="areaMin")
min_pow.send_keys("55")
max_pow = driver.find_element(By.ID, value="areaMax")
max_pow.send_keys("80")

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

time.sleep(1) # zmienić na Wait Until Load
# linki do ofert oferty
link_elements_list = driver.find_elements(By.CLASS_NAME, value="css-lsw81o")
links_list = []
for element in link_elements_list:
    links_list.append(element.get_attribute("href"))
    print(element.get_attribute("href"))

row_dict = {}

for link in links_list[:1]:
    driver.get(link)
    time.sleep(1)
    try:
        title = driver.find_element(By.XPATH, value='//*[@id="__next"]/main/div[2]/div[2]/header/h1')
        print(title.text)
    except:
        title = None
        print(title)

    price = driver.find_element(By.CLASS_NAME, value="css-t3wmkv")
    print(price.text)
    price_sqm = driver.find_element(By.CLASS_NAME, value='css-1h1l5lm')
    print(price_sqm.text)


    size_m2 = driver.find_element(By.CSS_SELECTOR, value='[data-testid="table-value-area"]')
    print(size_m2.text)

    #size_m2 = driver.find_element(By.CLASS_NAME, value="css-1wi2w6s")
    #print(size_m2.text)

    n_rooms = driver.find_element(By.CSS_SELECTOR, value='[data-testid="table-value-rooms_num"]')
    print(n_rooms.text)
    #n_rooms = driver.find_element(By.CLASS_NAME, value="css-19yhkv9")
    #print(n_rooms.text)
    floor = driver.find_element(By.CSS_SELECTOR, value='[data-testid="table-value-floor"]')
    print(floor.text)
    ownership_type = driver.find_element(By.CSS_SELECTOR, value='[data-testid="table-value-building_ownership"]')
    print(ownership_type.text)

    try:
        condition = driver.find_element(By.CSS_SELECTOR, value='[data-testid="table-value-construction_status"]')
        print(condition.text)
    except:
        condition = None
        print(condition)

    outdoor = driver.find_element(By.CSS_SELECTOR, value='[data-testid="table-value-outdoor"]')
    print(outdoor.text)
    try:
        heating = driver.find_element(By.CSS_SELECTOR, value='[data-testid="table-value-heating"]')
        print(heating.text)
    except:
        heating = None
        print(heating)

    market_type = driver.find_element(By.CSS_SELECTOR, value='[data-testid="table-value-market"]')
    print(market_type.text)
    advertiser_type = driver.find_element(By.CSS_SELECTOR, value='[data-testid="table-value-advertiser_type"]')
    print(advertiser_type.text)
    build_year = driver.find_element(By.CSS_SELECTOR, value='[data-testid="table-value-build_year"]')
    print(build_year.text)
    building_type = driver.find_element(By.CSS_SELECTOR, value='[data-testid="table-value-building_type"]')
    print(building_type.text)
    windows_type = driver.find_element(By.CSS_SELECTOR, value='[data-testid="table-value-windows_type"]')
    print(windows_type.text)
    elevator = driver.find_element(By.CSS_SELECTOR, value='[data-testid="table-value-lift"]')
    print(elevator.text)
    security_type = driver.find_element(By.CSS_SELECTOR, value='[data-testid="table-value-security_types"]')
    print(security_type.text)
    equipment_type = driver.find_element(By.CSS_SELECTOR, value='[data-testid="table-value-equipment_types"]')
    print(equipment_type.text)
    add_info = driver.find_element(By.CSS_SELECTOR, value='[data-testid="table-value-extras_types"]')
    print(add_info.text)
    building_material = driver.find_element(By.CSS_SELECTOR, value='[data-testid="table-value-building_material"]')
    print(building_material.text)


    #break


