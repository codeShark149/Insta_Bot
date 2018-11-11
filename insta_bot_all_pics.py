from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

def handle_dialog(wait):
#handle the popup box
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]')))
    turn_on_button = element.find_element(By.XPATH, '//button[@class="aOOlW  bIiDR  "]')
    turn_on_button.click()
    close_button = element.find_element(By.XPATH, '//button[@class="_0mzm- dCJp8"]')
    close_button.click()


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
        handle_dialog(wait)
        return driver

    def like_photo(self, hashtag):
        #login into server
        driver = self.login()
        #same old waiting function
        wait = WebDriverWait(driver, 10)
                
        #Get the sreach box and type in the hashtag
        search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        search_box.clear()
        search_box.send_keys(hashtag)

        #wait for the drop down list and click on the first entry
        drop_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="fuqBx"]')))
        drop_box_links = drop_box.find_elements_by_tag_name('a')
        drop_box_links[0].click()

        #wait for the search result and catch all the pics in the current window
        article = wait.until(EC.presence_of_element_located((By.XPATH, '//article[@class="KC1QD"]')))
        current_rows = article.find_elements(By.XPATH, '//div[@class="Nnq7C weEfm"]')
        #execute like in each pics of the "Top Post" section
        for row in current_rows:
            updated_row_list = []
            #scrol the pic for errorless clicking
            driver.execute_script("arguments[0].scrollIntoView();",row)

            #update the artcile due to scrolling
            article = driver.find_element(By.XPATH, '//article[@class="KC1QD"]')
            updated_row_list = article.find_elements(By.XPATH, '//div[@class="Nnq7C weEfm"]')
            for new_row in updated_row_list:
                if not new_row in current_rows:
                    current_rows.append(new_row)

            pics_in_row = row.find_elements_by_tag_name('a')
            for pic in pics_in_row:
                pic.click()
                #get the pic dialog box
                pic_dialog = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="_97aPb "]')))
                #catch the close button
                close_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="ckWGn"]')))
                #catch the like button
                like_button = pic_dialog.find_element(By.XPATH, '//span[@class="fr66n"]')
                like_button.click()
                close_button.click()

saptarshi = InstagramBot("username","password")
saptarshi.like_photo('hashtag')

#saptarshi.closeBrowser()
