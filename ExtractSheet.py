# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Extract2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://import.io/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_extract2(self):
        driver = self.driver
        driver.get(self.base_url + "/sign-in/?returnPath=data%2Fmine%2F")
        driver.find_element_by_link_text("use your existing username").click()
        driver.find_element_by_xpath("//input[@type='text']").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("mtmarin84@gmail.com")
        driver.find_element_by_xpath("//input[@type='text']").send_keys(Keys.SPACE)
        driver.find_element_by_xpath("(//input[@type='password'])[2]").click()
        driver.find_element_by_xpath("(//input[@type='password'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys("280684")
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys(Keys.SPACE)
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys(Keys.TAB)
        driver.find_element_by_css_selector("div.passwordContainer > div.buttons > a.btn.btn-primary").click()
        for i in range(60):
            try:
                if "New..." == driver.find_element_by_link_text("New...").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if self.is_element_present(By.LINK_TEXT, "New..."): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "New..."))
        driver.find_element_by_link_text("New...").click()
        driver.get("https://magic.import.io/")
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "//input[@type='text']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("www.udemy.com")
        driver.find_element_by_id("get-data").click()
        driver.find_element_by_xpath("//nav[@id='footer-toolbar']/automagic-actions/div[2]/button[2]").click()        
        driver.find_element_by_xpath("//div/div/button").click()       
        driver.find_element_by_link_text("Export").click()
        driver.find_element_by_css_selector("button.export-button").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
