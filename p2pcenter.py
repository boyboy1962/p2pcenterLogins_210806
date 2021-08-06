from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def p2pcenter(driver):
    driver.get('https://www.p2pcenter.or.kr/serviceintro/registrationCompanies')
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div/div[2]/table/thead/tr/th[4]/button')
        )
    )
    driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[2]/div/div/div[2]/table/thead/tr/th[4]/button').click()