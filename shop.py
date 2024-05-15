import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
driver = webdriver.Chrome(options=options)

# 要搶的頁面
driver.get('https://shopee.tw/product/64611424/22936066958?d_id=39ed1&utm_content=2anr2m7aVuno4BUWrGKS6LHdpfDR&is_from_login=true')

def do1():
    button_selector = "button[aria-label='櫻花粉']"
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector))).click()
    print("已選擇櫻花粉")

def do2():
    time.sleep(0.065)
    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-solid-primary.btn--l.iFo-rx"))).click()
    print("已點選直接購買")

def do3():
    time.sleep(0.065)
    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='shopee-button-solid shopee-button-solid--primary']"))).click()
    print("已點選去買單")

def do4():
    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.stardust-button.stardust-button--primary.stardust-button--large.apLZEG"))).click()
    print("已點選下訂單")

do1()
#do2()
#do3()
#do4()
