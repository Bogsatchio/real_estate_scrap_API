import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

###
# ENDPOINTS
# - search for books by (title / title and author) in all stores
# - search for book by (title / title and author) in selected store
# - s

###
SEARCH_PHRASE = "flow"

# Keep Chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.empik.com/ksiazki")
search_bar = driver.find_element(By.XPATH, value='/html/body/header/div/div/div[3]/div/div/form/div/div[1]/input')
search_bar.send_keys(SEARCH_PHRASE, Keys.ENTER)

time.sleep(1)
cookies_accept = driver.find_element(By.XPATH, value='/html/body/div[3]/div/div[2]/div[2]/div[1]/div/button[1]')
cookies_accept.click()

books_category = driver.find_elements(By.XPATH, value='/html/body/main/div[2]/div/div/div/div[1]/div[1]/div[2]/div/ul/li/a')
for element in books_category:
    if "Książki" in element.text and "Książki o" not in element.text:
        element.click()
        break
#books_category.click()
tiles = driver.find_elements(By.XPATH, value='/html/body/main/div[2]/div/div/div/div[2]/div[2]/div[4]/div/div')
titles_list = []
authors_list = []
for element in tiles:
    try:
        title = element.find_element(By.CLASS_NAME, value="product-title")
        titles_list.append(title.text)
        author_scrap_list = element.find_elements(By.CLASS_NAME, value="smartAuthor ")
        if len(author_scrap_list) == 1:
            #print(author_scrap_list[0].text)
            #print(type(author_scrap_list[0].text))
            authors_list.append(author_scrap_list[0].text)
        else:
            author_name_list = [elem.text for elem in author_scrap_list]
            #print(author_name_list)
            #print(type(author_name_list))
            authors_list.append(author_name_list)

    except:
        continue
print(titles_list)
print(authors_list)

