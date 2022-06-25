from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_drive_path = "/Users/killsamurai/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.get("https://orteil.dashnet.org/cookieclicker/")


def check_cookies():
    cookie_count = driver.find_element(By.ID, "cookies")
    split = cookie_count.text.split()
    amount = split[0]
    check_purchase(int(amount))


def check_purchase(amount):
    grandma = driver.find_element(By.ID, "productPrice1")
    price_grandma = int(grandma.text)
    if amount >= price_grandma:
        click_grandma = driver.find_element(By.ID, "product1")
        click_grandma.click()
    else:
        click_cursor = driver.find_element(By.ID, "product0")
        click_cursor.click()

language = driver.find_element(By.CSS_SELECTOR, "#langSelect-EN")
language.click()

cookie = driver.find_element(By.ID, "bigCookie")

game_on = True

while game_on:
    cookie.click()
    check_cookies()








