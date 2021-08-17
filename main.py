import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time



PATH = "C:\chromedriver.exe"
EMAIL = "EMAIL"
PASS = "PASSWORD"
crs = "2022 TCS Ninja Preparatory Course"
test = "2022_TCS Ninja Mock Test 5"
stage_name = "Mock Tests"
multiple_test = True
driver = webdriver.Chrome(PATH)
driver.get("https://tpc.kcgcollege.ac.in/")
driver.maximize_window()
time.sleep(2)

def take_test_random():
    opt,blk,prg = True,True,True
    try:
        options = driver.find_elements(By.XPATH,"//div[contains(@id,'tt-option-')]")
    except:
        opt=False
        print("Not MCQ")
    try:
        blank = driver.find_elements(By.XPATH,"//div[contains(@id,'tt-answer-33-fillup-blank-')]")
    except:
        blk = False
        print("Not a Blank")
    #try:
    #    program = driver.find_elements_by_xpath("//div[@class='programming-container']")
    #except:
    #    prg = False

    program = WebDriverWait(driver, 5 , ignored_exceptions=('NoSuchElementException','StaleElementReferenceException')).until(EC.presence_of_element_located(By.CLASS_NAME,'programming-container'))
    if(len(program)):
        pass
    else:
        prg = False
        print("Not a program")

    try:
        
        next_button = driver.find_element_by_id("tt-footer-next")
        if(opt):
            actions = ActionChains(driver)
            actions.move_to_element(options[random.randint(0,len(options)-1)])
            actions.click()
            actions.perform()
        elif(blk):
            blank.send_keys("dont know")
        elif(prg):
            pass
        actions = ActionChains(driver)
        actions.move_to_element(next_button)
        actions.click()
        actions.perform()
    except:
        return


try:

    login_email = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    login_email.send_keys(EMAIL)
    login_email.send_keys(Keys.RETURN)

    login_pass = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    login_pass.send_keys(PASS)
    login_pass.send_keys(Keys.RETURN)

    hamburger = WebDriverWait(driver , 100).until(
        EC.presence_of_element_located((By.XPATH,"//div[@class='container hambur icon-navicon ng-star-inserted']"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(hamburger)
    actions.perform()

    select_course = WebDriverWait(driver , 100).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/app-root/div/app-top-header/div/div[1]/div[1]/div[2]/div/div[3]/div[2][@class='padleft10']"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(select_course)
    actions.click()
    actions.perform()

    time.sleep(5)
    list_courses = driver.find_elements_by_xpath("//div[@class='font18 fw500 myctitle mycmarg']")
    for i in list_courses:
        if(i.text == crs):
            selected_course = i

    actions = ActionChains(driver)
    actions.move_to_element(selected_course)
    actions.click()
    actions.perform()
    time.sleep(5)
    if(multiple_test):
        stages = driver.find_elements(By.XPATH,"//div[@class='acdtitle fw500 font16']")
        for i in stages:
            if(i.text == stage_name):
                actions = ActionChains(driver)
                actions.move_to_element(i)
                actions.click()
                actions.perform()
    time.sleep(5)
    list_test = driver.find_elements_by_xpath("//div[@class='accEach1 ng-star-inserted']")
    for i in list_test:
        if(i.text.split("\n")[1] == test):
            actions = ActionChains(driver)
            actions.move_to_element(i)
            actions.click()
            actions.perform()
    
    time.sleep(3)
    take_test = driver.find_element_by_xpath("//button[contains(@id, 'undefined')]")
    if(take_test.text == "Test Completed"):
        print("Test already Completed")
        driver.quit()
    else:
        actions = ActionChains(driver)
        actions.move_to_element(take_test)
        actions.click()
        actions.perform()
        time.sleep(3)
        actions = ActionChains(driver)
        actions.move_to_element(driver.find_element_by_id("tt-start-accept"))
        actions.click()
        actions.perform()
        time.sleep(60)
        rem_q = driver.find_elements_by_xpath("//div[@class='each-section-summary ng-star-inserted']")
        nn = int(rem_q[len(rem_q)-1].text.split("\n")[1])
        time.sleep(1)
        while(nn):
            rem_q = driver.find_elements_by_xpath("//div[@class='each-section-summary ng-star-inserted']")
            nn = int(rem_q[len(rem_q)-1].text.split("\n")[1])
            time.sleep(3)
            take_test_random()
            if(nn == 0):
                nn += 1
        time.sleep(2)
        actions = ActionChains(driver)
        actions.move_to_element(driver.find_element_by_xpath("//button[@id='tt-header-submit']"))
        actions.click()
        actions.perform()
        time.sleep(2)
        driver.find_element_by_id("name").send_keys("END")
        time.sleep(2)
        actions = ActionChains(driver)
        actions.move_to_element(driver.find_element_by_xpath("//button[@id='undefinedYes1']"))
        actions.click()
        actions.perform()
        time.sleep(20)

except Exception as e:
    print("Oops!", e.__class__, "occurred.")
    print("Exiting")
    driver.quit()


