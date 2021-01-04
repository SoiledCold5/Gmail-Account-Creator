from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import string
import pyautogui


def random_generator(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def type_slow(value,speed):
    sentense = value
    for i in range(len(sentense)):
        pyautogui.press(sentense[i])
        time.sleep(speed)
        
first_name = random.choice(("Super", "Epicer", "Great", "Sexy", "Vegan", "Brave", "Shy", "Cool", "Poor", "Rich", "Fast", "Gummy", "Yummy", "Masked", "Unusual", "American", "Bisexual", "MLG", "Mlg", "lil", "Lil"))
last_name = random.choice(("Coder", "Vegan", "Man", "Attacker", "Horse", "Bear", "Goat", "Goblin", "Learner", "Frost", "Woman", "Programmer", "Spy", "Hause", "Spooderman", "Carrot", "Goat", "Quickscoper", "Quickscoper"))
password = random_generator(10)

driver = webdriver.Chrome("driver")
driver.get("https://accounts.google.com/embedded/setup/android/createaccount?source=com.android.settings&xoauth_display_name=Android%20Phone&imsi=410060265624275&canSk=1&lang=en&langCountry=en_us&hl=en-US&cc=pk&use_native_navigation=0&flowName=EmbeddedSetupAndroid")

# Click On Create Account Button For My Self
time.sleep(3)
create_new = driver.find_element_by_xpath("//*[@id='ow276']")
create_new.click()

time.sleep(1)
my_self = driver.find_element_by_class_name("jO7h3c")
my_self.click()
time.sleep(4)
# Enter The Personal Details

fname = driver.find_element_by_xpath('//*[@id="firstName"]').click()
type_slow(first_name,0.5)
time.sleep(1)
lname = driver.find_element_by_xpath('//*[@id="lastName"]').click()
type_slow(last_name,0.5)
time.sleep(1)
next_button = driver.find_element_by_xpath('//*[@id="collectNameNext"]')
next_button.click()
