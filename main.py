'''
Created on 2021. 8. 5.

@author: USER
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from datetime import datetime
import winsound
import time
import math
import p2pcenter
import eightPercent

email = input("이메일을 입력해주세요: ")
ID = email[0:10]
PW = input('비밀번호를 입력해주세요: ')
driver = webdriver.Chrome('C:\chromedriver.exe')

p2pcenter.p2pcenter(driver)
eightPercent.eight_percent_login(driver, email, PW)