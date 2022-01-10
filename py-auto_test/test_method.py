import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    chromedriverPath = '/home/dev/programs/chromedriver'
    driver = webdriver.Chrome(executable_path=chromedriverPath)

    driver.get("http://127.0.0.1:5500/inputs/index.html")
    driver.maximize_window()
    time.sleep(1)

    phoneInput = driver.find_element(By.XPATH, "//html/body/input[1]")
    phoneInput.send_keys("89777751713")
    time.sleep(1)

    termsCheckbox = driver.find_element(By.XPATH, "//html/body/input[2]")
    termsCheckbox.click()
    time.sleep(1)


    driver.quit()


if __name__ == '__main__':
    main()
