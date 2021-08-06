
def eight_percent_login(driver, ID, PW):
    driver.execute_script('window.open("https://8percent.kr/user/login/")')
    driver.switch_to.window(driver.window_handles[1])

    driver.find_element_by_id('textfield').send_keys(ID)
    driver.find_element_by_id('textfield-509').send_keys(PW)
    driver.find_element_by_id('remember_me').click()
    driver.find_element_by_id("submitbutton").click()