import time


def people_fund_login(driver, ID, PW):
    driver.execute_script('window.open("https://www.peoplefund.co.kr/auth/login")')
    driver.switch_to.window(driver.window_handles[2])

    driver.find_element_by_xpath('//*[@id="pf-login"]/div[2]/div/form/div[1]/div[1]/div/input').send_keys(ID)
    driver.find_element_by_xpath('//*[@id="pf-login"]/div[2]/div/form/div[1]/div[2]/div[1]/input').send_keys(PW)
    driver.find_element_by_id('checkbox-save-email').click()
    driver.find_element_by_xpath('//*[@id="pf-login"]/div[2]/div/form/div[1]/button').click()

    time.sleep(3)   # 너무 빨리 넘어가서 약간의 쉬는 시간을 가짐
    # 피플펀드의 나의 투자 현황 페이지로 넘긴다.
    driver.get('https://www.peoplefund.co.kr/mypage/invest#menu=dashboard&listType=showcase&listStatus=%EC%A0%84%EC%B2%B4')
