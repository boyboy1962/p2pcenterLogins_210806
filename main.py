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
import people_fund

ID = input("아이디를 입력해주세요: ")
email = ID + "@gmail.com"
PW = input('비밀번호를 입력해주세요: ')
driver = webdriver.Chrome('C:\chromedriver.exe')

driver.maximize_window() # 대화면 크기

p2pcenter.p2pcenter(driver)                         # 가장 먼저 로딩하는 P2P 공인정부관리기관
eightPercent.eight_percent_login(driver, email, PW) # 8퍼센트 로그인
people_fund.people_fund_login(driver, email, PW)    # 피플펀드 로그인