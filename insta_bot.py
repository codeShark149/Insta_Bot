from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

class InstagramBot:
    

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        #define a waiting function
        wait = WebDriverWait(driver, 10)
        driver.get("https://www.instagram.com/accounts/login/")
        #Wait for username box to appear
        username_elem =wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        username_elem.clear()
        username_elem.send_keys(self.username)
        password_elem = driver.find_element_by_name("password")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        return driver

    def like_photo(self, hashtag):
        #login into server
        driver = self.login()
        #same old waiting function
        wait = WebDriverWait(driver, 10)
        #handle the popup box, carry on if doesnt appear 
        try:
            element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]')))
            buttons = element.find_elements_by_tag_name('button')
            buttons[0].click()
        except:
            pass
        
        #Get the sreach box and type in the hashtag
        search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        search_box.clear()
        search_box.send_keys(hashtag)

        #wait for the drop down list and click on the first entry
        drop_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="fuqBx"]')))
        drop_box_links = drop_box.find_elements_by_tag_name('a')
        drop_box_links[0].click()

        #wait for the search result and only catch the pics in "Top Post" section
        top_post_division = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="EZdmt"]')))
        top_pics = top_post_division.find_elements_by_tag_name('a')

        #execute like in each pics of the "Top Post" section
        for pic in top_pics:
            #scrol the pic for errorless clicking
            driver.execute_script("arguments[0].scrollIntoView(true);",pic)
            pic.click()
            #get the pic dialog box
            pic_dialog = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="_97aPb "]')))
            #catch the close button
            close_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="ckWGn"]')))
            #catch the like button
            like_button = pic_dialog.find_element(By.XPATH, '//span[@class="fr66n"]')
            #scroll like button to view, may not be necessary
            driver.execute_script("arguments[0].scrollIntoView(true);",like_button)
            time.sleep(1)#delay added only for visual purpose 
            like_button.click()
            time.sleep(1)#delay added only for visual purpose
            close_button.click()

        #a refernce of how to get the content of a tag
        # not important for the bot.    
        #popup_text = element.find_element(By.TAG_NAME, 'h2').get_attribute('innerHTML')
        

saptarshi = InstagramBot("rajarshi149","Rajarshi_149")
saptarshi.like_photo('pujadays')
saptarshi.closeBrowser()
