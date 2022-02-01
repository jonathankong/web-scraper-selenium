import time

import webdriver from selenium


driver = webdriver.Chrome(r'C:\\chromedriver\\chromedriver.exe') # Optional argument, if not specified will search path.

driver.get('https://www.nintendo.com/en_CA/games/game-guide/#filter/:q=&dFR[generalFilters][0]=Deals');

time.sleep(5) # Let the user actually see something!

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# loadMoreGamesButton = driver.find_elements_by_class_name('Load more games')

time.sleep(5) # Let the user actually see something!

driver.quit()