import time

from selenium import webdriver


driver = webdriver.Chrome(r'C:\\chromedriver\\chromedriver.exe') # Optional argument, if not specified will search path.

driver.get('https://www.nintendo.com/en_CA/games/game-guide/#filter/:q=&dFR[generalFilters][0]=Deals');

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()