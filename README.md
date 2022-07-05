# 5_time
方法更新的尼玛真快
import requests
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://appckddwtqm7716.pc.xiaoe-tech.com/training/privilege/resource/get_courses?app_id=appckddwtqm7716&app_id=appckddwtqm7716&user_id=u_wework_62b95f9e91b92_aa88EAe3SbHDEmHH&page_size=300&page_index=1"
htmlbody = requests.get(url)
result = json.loads(htmlbody.text)['data']['currentPageSearchResults']
len(result)  # 300课

# 清洗数据
title = []
jump_url = []
type = []
time = []
for i in range(len(result)):
    if result[i]['type'] != 4:
        title.append(result[i]['title'])
        jump_url.append('https://appckddwtqm7716.pc.xiaoe-tech.com' + result[i]['jump_url'])
        type.append(result[i]['type'])
        print(i)

result_af = pd.concat([pd.DataFrame(title), pd.DataFrame(jump_url), pd.DataFrame(type)], axis=1)

result_af.to_csv('result_300.csv', encoding='utf_8_sig')
def look(url, title):
    driver = webdriver.Chrome()
    driver.set_window_size('500', '500')
    driver.get(url)
    time.sleep(3)
    driver.find_element(by=By.CLASS_NAME, value='login-phone').click()
    user_input = driver.find_element(by=By.XPATH, value='//input[@type="text"]')
    pw_input = driver.find_element(by=By.XPATH, value='//input[@type="password"]')
    # 输入用户名和密码，点击登录
    user_input.send_keys("###")
    pw_input.send_keys("###")
    driver.find_element(by=By.XPATH, value='//button').click()
    # 获取学习进度
    time.sleep(5)
    text1 = driver.find_element(by=By.CLASS_NAME, value='vjs-current-time-display').get_attribute('textContent')
    text2 = driver.find_element(by=By.CLASS_NAME, value='vjs-duration-display').get_attribute('textContent')
    timebegin = 0
    timeover = 0
    if len(text1.split(':')) == 2:
        timebegin = int(text1.split(':')[1]) + int(text1.split(':')[0]) * 60
    if len(text1.split(':')) == 3:
        timebegin = int(text1.split(':')[2]) + int(text1.split(':')[1]) * 60 + int(text1.split(':')[0]) * 60

    if len(text2.split(':')) == 2:
        timeover = int(text2.split(':')[1]) + int(text2.split(':')[0]) * 60
    if len(text2.split(':')) == 3:
        timeover = int(text2.split(':')[2]) + int(text2.split(':')[1]) * 60 + int(text2.split(':')[0]) * 3600
    # driver.find_element(by=By.CLASS_NAME, value='vjs-tech').send_keys(Keys.SPACE)
    driver.minimize_window()
    if timebegin > 0:
        print("开始学习：\"" + title + "\" 学习时间为：" + str(timeover - timebegin) + "秒")
        time.sleep(timeover - timebegin)
    else:
        print("开始学习：\"" + title + "\" 学习时间为：3600秒")
        time.sleep(3600)
    driver.quit()
