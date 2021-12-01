from selenium import webdriver
import pandas as pd
import time
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver=webdriver.Firefox()
driver.get("https://www.csclocator.com/csc/orissa/")
w=WebDriverWait(driver,8)
w.until(expected_conditions.presence_of_element_located((By.ID,"district")))
district_ele=driver.find_element_by_id("district")
district_drop=Select(district_ele)
all_dist=[]
for i in district_drop.options:
	all_dist.append(i.text)

print(all_dist)

for i in range(1,3):
	district_drop.select_by_visible_text(all_dist[i])
	w.until(expected_conditions.presence_of_element_located((By.ID,"block")))
	block_ele=driver.find_element_by_id("block")
	block_drop=Select(block_ele)
	all_block=[]
	for i in block_drop.options:
		all_block.append(i.text)

	for j in range(1,3):
		block_drop.select_by_visible_text(all_block[j])
		driver.back()
		w.until(expected_conditions.presence_of_element_located((By.ID,"block")))
		block=driver.find_element_by_id('block')
		block_drop=Select(block)

	driver.back()
	w.until(expected_conditions.presence_of_element_located((By.ID,"district")))
	district_ele=driver.find_element_by_id("district")
	district_drop=Select(district_ele)


