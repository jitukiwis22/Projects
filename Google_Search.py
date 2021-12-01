from selenium import webdriver
import pandas as pd
import time
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

#Open the Firefox browser
driver=webdriver.Firefox()

#driver.get("https://www.google.com/search?sa=X&tbs=lf:1,lf_ui:2&tbm=lcl&sxsrf=ALeKk03e2YhLX6xk-TJWo4Mk2eXXxOrbbw:1620834875564&q=hospitals+in+bhubaneswar&rflfq=1&num=10&ved=2ahUKEwi6hv23wMTwAhVDQH0KHcAXDwIQjGp6BAgGEGM&biw=1920&bih=895#rlfi=hd:;si:;mv:[[20.3406988,85.8830998],[20.2360927,85.7631962]];start:40")
driver.get("https://google.com")

#Find the search bar in Google
searchbar=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
searchbar.send_keys("Hospital in bhubaneswar",Keys.ENTER)

#Wait for 8 seconds to load the page 
w=WebDriverWait(driver,8)

#Wait for the particular Class_Name to be load while the page load
w.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"MXl0lf")))
driver.find_element_by_class_name("MXl0lf").click()

w.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"cXedhc")))
time.sleep(3)
stores=driver.find_elements_by_class_name('cXedhc')

#Print total no. of items available in One single page
print(len(stores))

Name=[]             #Store the Name in this list
Address=[]          #Store the Address in this list
Contact=[]          #Store the Contact in this list


#In this loop iterate through all the items
for i in range(len(stores)):

    #Click on the perticular item show on the google search results
    stores[i].find_element_by_class_name('dbg0pd').click()
    time.sleep(5)
    w1=WebDriverWait(driver,8)
    w1.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"xpdopen")))
    full=driver.find_element_by_class_name('xpdopen')
    name=full.find_element_by_class_name('qrShPb').text
    addr=full.find_element_by_class_name('LrzXr').text
    try:
        #Some of the items dont have the contact 
    	phone=full.find_element_by_class_name('zdqRlf').text
    except:
        #Those have no contacts 
    	phone="No Contact Found"
    
    Name.append(name)
    Address.append(addr)
    Contact.append(phone)

time.sleep(2)


#Users Input
total_page=4

#Iterate through next pages upto users input 
for j in range(total_page):
    #Click on Next Page
    driver.find_element_by_xpath('/html/body/div[6]/div/div[8]/div[1]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[12]/a/span[2]').click()
    w.until(expected_conditions.presence_of_element_located((By.XPATH,"/html/body/div[6]/div/div[8]/div[1]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[12]/a/span[2]")))
    time.sleep(2)
    w.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"cXedhc")))
    stores=driver.find_elements_by_class_name('cXedhc')
    print(len(stores))

    #This loop same as the loop in line 40 
    for i in range(len(stores)):
        stores[i].find_element_by_class_name('dbg0pd').click()
        time.sleep(5)
        w1=WebDriverWait(driver,8)
        w1.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"xpdopen")))
        full=driver.find_element_by_class_name('xpdopen')
        name=full.find_element_by_class_name('qrShPb').text
        addr=full.find_element_by_class_name('LrzXr').text
        try:
            phone=full.find_element_by_class_name('zdqRlf').text
        except:
            phone="No Contact Found"
        
        Name.append(name)
        Address.append(addr)
        Contact.append(phone)



#Here I defining the dataset
data={"Name":Name,"Address":Address,"Contact":Contact}
df= pd.DataFrame(data)
df.to_csv('Demo.xlsx',index=False)

driver.close()
