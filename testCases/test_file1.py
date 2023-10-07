import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
service_obj = Service()

class Test_py:
    def test_sum_001(self): #item:--> Test Cases --> start with 'test_'
        a = 3
        b = 5
        sum = a + b

        if sum == 8:
            print("test_sum_001 is Passed")
            assert True

        else:
            print("test_sum_001 is Failed")
            assert False


    def test_mul_002(self):
        a = 3
        b = 5
        mul = a * b
        print(mul)

        if mul == 16:

            print("test_mul_002 is Passed")
            assert True

        else:
            print("test_mul_002 is Failed")
            assert False

    def sum_002(self): # this item/function/testcase will not consider as testcase because of name
        a = 3
        b = 5
        sum = a + b
        print(sum)

        if sum == 8:

            print("sum_002 is Passed")
            assert True

        else:
            print("sum_002 is Failed")
            assert False

    @pytest.mark.group1
    def test_google(self):
        driver = webdriver.Chrome(options = chrome_options)
        driver.get("https://www.google.com/")
        logo = driver.find_element(By.CLASS_NAME,"lnXdpd").is_displayed()
        print(logo)
        if logo == True:
            driver.close()
            assert True
        else:
            driver.close()
            assert False



