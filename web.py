'''1st assesment - CNN Australia News Scaper'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_argument("--incognito")

'''Create new Insatnce of Chrome in incognito to mode'''
browser = webdriver.Chrome (executable_path= 'C:\webdrivers\chromedriver',options = option)


'''Set up website url '''
browser.get("https://www.cnn.com/australia")
    
'''Find the news'''
titles_element = browser.find_elements_by_xpath("//a[@class='text-bold']")
headline = [x.text for x in titles_element]

'''Print Headline'''
if len(headline) == 0:
    print ("None")
else:
    print ("Headline: ")
    for title in headline:
        print (title)
    
    
    
    
