import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class Test_web:
    def test_credence(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        time.sleep(2)
        driver.find_element(By.XPATH,"//img[@src='/website/images/enquiry.png']").click()
        time.sleep(2)
        l = len(driver.find_element(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p//a").text)
        print(l,"is length")
        list = []
        for r in range (1,l+1):
            contact = driver.find_element(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p//a["+str(r)+"]")
            print(contact)
            list.append(contact)
        if "+91 9091929355" in list:
            assert True
        else:
            assert False

