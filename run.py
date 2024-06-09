import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pymongo import MongoClient
import datetime
from dotenv import load_dotenv

load_dotenv()

os.environ['PATH'] += r"C:\seleniumDrivers"



options = webdriver.ChromeOptions()
# without these options chrome will open and then close automatically
options.add_experimental_option("detach", True)

# opens the chrome browser
driver=webdriver.Chrome(options=options)

# open a page in chrome
driver.get("https://x.com/i/flow/login")

driver.implicitly_wait(5)



username_input=driver.find_element(By.CLASS_NAME,'r-30o5oe')
username_input.send_keys(os.getenv("TWITTER_USERNAME"))

next_btn1=driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
next_btn1.click()

password_input=driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password_input.send_keys(os.getenv('TWITTER_PASSWORD'))

login_btn=driver.find_element(By.CSS_SELECTOR,'button[data-testid="LoginForm_Login_Button"]')
login_btn.click()

# now go to trandings page and fetch top 5 posts
time.sleep(5)
driver.get("https://x.com/explore")

allSection_element=driver.find_elements(By.CSS_SELECTOR,'div[data-testid="trend"]')

topTrends=[]
j=0
for i in allSection_element:
    trend=i.find_element(By.XPATH,'.//div/div[2]/span')
    text=trend.get_attribute("innerText")
    topTrends.append(text)
    if j==4:
        break
    else:
        j=j+1



# store the rends in mongoDB database

client=MongoClient("localhost",27017)
db=client.TwitterBotDB

trendings=db.trendings

nameOfTrends={
        "nameoftrend1": topTrends[0],
        "nameoftrend2": topTrends[1],
        "nameoftrend3": topTrends[2],
        "nameoftrend4": topTrends[3],
        "nameoftrend5": topTrends[4],
        "timestamp": datetime.datetime.now()
    }
trendings.insert_one(nameOfTrends)
