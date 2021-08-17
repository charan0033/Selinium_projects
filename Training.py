import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
def main(End_time):
    driver.get("https://event.webinarjam.com/go/live/12/yg4o9bzf0s1sr")
    driver.maximize_window()
    no_cap = False
    time.sleep(2)
    try:
        time.sleep(3)
        name = driver.find_element_by_xpath("//input[@placeholder='First name...']")
        email = driver.find_element_by_xpath("//input[@placeholder='Email...']")
        register_button = driver.find_element_by_xpath("//button[@id='register_btn']")
        try:
            cap = driver.find_element_by_xpath("//input[@placeholder='Enter captcha...']")
            cap.send_keys("Enter captcha...")
        except:
            no_cap = True
        if(no_cap):
            time.sleep(3)
            name.send_keys("NAME")
            email.send_keys("EMAIL")
            actions = ActionChains(driver)
            actions.move_to_element(register_button)
            actions.click()
            actions.perform()
            while(int(End_time.split(":")[0]) >= (time.localtime().tm_hour)):
                if(int(End_time.split(":")[0]) == (time.localtime().tm_hour)):
                    if(int(End_time.split(":")[1]) <= (time.localtime().tm_min)):
                        break
                    else:
                        pass
                else:
                    pass
        else:
            driver.quit()
    except Exception as e:
        print("Exiting")
        print(e.__class__+" Occurred")
        driver.quit()
