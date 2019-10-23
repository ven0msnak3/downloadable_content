import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('insert choice of URL here.')

#no_of_pagedowns = 20
#
#while no_of_pagedowns:
#    elem.send_keys(Keys.PAGE_DOWN)
#    time.sleep(0.2)
#    no_of_pagedowns-=1

#names = browser.find_elements(By.XPATH, '//a[@class="listing__name--link listing__link jsListingName"]')
#name = [x.text for x in names]
#print(name)

phones = browser.find_elements_by_tag_name('insert choice of tag here.')
val = phones.get_attribute("insert choice of attribute here.")
browser.quit()
