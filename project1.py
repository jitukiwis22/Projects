from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import time

#start the chromedriver for testing
driver=webdriver.Chrome("/home/rajesh/Desktop/python/intern/project1/chrome_driver/chromedriver")

#location="Mumbai"
#aoi="Hotels"
#url="https://justdial.com/"+location+"/"+aoi+"/"


#Fetch the url in the automated control browser
driver.get("https://justdial.com/mumbai/hotels")

#this function convert the string to number for contact
def convert_num(argument): 
    
    switcher = { 
        'dc': '+',
        'fe': '(',
        'hg': ')',
        'ba': '-',
        'acb': '0', 
        'yz': '1', 
        'wx': '2',
        'vu': '3',
        'ts': '4',
        'rq': '5',
        'po': '6',
        'nm': '7',
        'lk': '8',
        'ji': '9'
    } 
    
    return switcher.get(argument, "nothing")

#scrol the webpage to end 
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#just wait for 15 sec to for completely load the side
time.sleep(15)

storeDetails = driver.find_elements_by_class_name('store-details')

nameList = []			#store the name of the aoi
addressList = []		#store the address of the aoi
numbersList = []		#store the contact of the aoi

for i in range(len(storeDetails)):
    
    name = storeDetails[i].find_element_by_class_name('lng_cont_name').text
    address = storeDetails[i].find_element_by_class_name('cont_fl_addr').get_attribute('innerHTML')
    contactList = storeDetails[i].find_elements_by_class_name('mobilesv')
    
    myList = []
    
    for j in range(len(contactList)):
        
        myString = contactList[j].get_attribute('class').split("-")[1]
    
        myList.append(convert_num(myString))

    nameList.append(name)
    addressList.append(address)
    numbersList.append("".join(myList))


    
# intialise data of lists.
data = {'Company Name':nameList,
        'Address': addressList,
        'Phone':numbersList}

# Create DataFrame
df = pd.DataFrame(data)

#store the dataframe into the excel sheet
df.to_csv("final.xlsx", index=False)