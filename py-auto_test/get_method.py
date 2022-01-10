import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By


def auto_main(driver, httpProtocol, mainHost):
    Path = "/"
    driver.get(httpProtocol+mainHost+Path)

    time.sleep(1)

    fromInput = driver.find_element(By.XPATH,"//div/section[2]/div/div/div/div/div[1]/div[1]")
    fromInput.click()
    time.sleep(1)

    listFrom = len(fromInput.find_elements(By.TAG_NAME, "li"))
    targetFrom = random.randint(1, listFrom)
    targetFromInput = fromInput.find_element(By.XPATH, "//div/section[2]/div/div/div/div/div[1]/div[1]/div/ul/li[{}]".format(targetFrom))
    targetFromInput.click()


    time.sleep(1)


    toInput = driver.find_element(By.XPATH,"//div/section[2]/div/div/div/div/div[1]/div[2]")
    toInput.click()
    time.sleep(1)

    listTo = len(toInput.find_elements(By.TAG_NAME, "li"))
    targetTo = random.randint(1, listTo)

    while targetTo == targetFrom:
        targetTo = random.randint(1, listTo)

    targetToInput = toInput.find_element(By.XPATH, "//div/section[2]/div/div/div/div/div[1]/div[2]/div/ul/li[{}]".format(targetTo))
    targetToInput.click()


    time.sleep(1)

    date_fromInput = driver.find_element(By.XPATH,"//div/section[2]/div/div/div/div/div[2]/div[1]/input")
    date_fromInput.click()
    time.sleep(1)

    date_toInput = driver.find_element(By.XPATH,"//div/section[2]/div/div/div/div/div[2]/div[2]/input")
    date_toInput.click()
    time.sleep(1)

    # findButton = driver.find_element(By.XPATH,"//div/section[2]/div/div/div/div/div[3]")
    # findButton.click()


def auto_login(driver, httpProtocol, mainHost):
    Path = "/login"
    driver.get(httpProtocol+mainHost+Path)
    time.sleep(1)

    # nameInput = driver.find_element(By.XPATH,"//div/main/div/div/div[2]/div/div/div/div[1]/input")
    # nameInput.send_keys("79777751713")
    time.sleep(10)

    codeBtn = driver.find_element(By.XPATH,"//div/main/div/div/div[2]/div/div/div/div[4]/button")
    codeBtn.click()
    time.sleep(5)

    codeInput = driver.find_element(By.XPATH,"//div/main/div/div/div[2]/div/div/div/div[2]/input")
    codeInput.send_keys("22222")
    time.sleep(1)

    loginBtn = driver.find_element(By.XPATH,"//div/main/div/div/div[2]/div/div/div/div[4]/button[1]")
    loginBtn.click()


def auto_profile(driver, httpProtocol, mainHost):
    Path = "/profile"
    driver.get(httpProtocol+mainHost+Path)


def auto_partners(driver, httpProtocol, mainHost):
    Path = "/partners"
    driver.get(httpProtocol+mainHost+Path)
    time.sleep(1)

    nameInput = driver.find_element(By.XPATH,"//div/main/div/div/div[1]/form/div/div[1]/input")
    nameInput.send_keys("Test")
    time.sleep(1)

    emailInput = driver.find_element(By.XPATH,"//div/main/div/div/div[1]/form/div/div[2]/input")
    emailInput.send_keys("test@gmail.com")
    time.sleep(1)

    phoneInput = driver.find_element(By.XPATH,"//div/main/div/div/div[1]/form/div/div[3]/input")
    phoneInput.send_keys("79777751713")
    time.sleep(1)

    infoInput = driver.find_element(By.XPATH,"//div/main/div/div/div[1]/form/div/div[4]/input")
    infoInput.send_keys("Some text about partner")
    time.sleep(1)

    termsCheckbox = driver.find_element(By.XPATH, "//div/main/div/div/div[1]/form/div/div[5]/label")
    termsCheckbox.value = "true"
    time.sleep(1)

    # sendButtom = driver.find_element(By.XPATH, "//div/main/div/div/div[1]/form/div/div[6]/button")
    # sendButtom.click()


def auto_service(driver, httpProtocol, mainHost):
    Path = "/service"
    driver.get(httpProtocol+mainHost+Path)


def auto_cart(driver, httpProtocol, mainHost):
    Path = "/cart"
    driver.get(httpProtocol+mainHost+Path)



def main():
    chromedriverPath = '/home/dev/programs/chromedriver'
    driver = webdriver.Chrome(executable_path=chromedriverPath)

    httpProtocol = "https://"
    mainHost = "devonshopnew.mileonair.com"
    driver.maximize_window()

    auto_login(driver, httpProtocol, mainHost)

    time.sleep(5)

    driver.quit()


if __name__ == '__main__':
    main()
