import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestMengaturstokbarang():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_mengaturstokbarang(self):
    # Test name: mengatur stok barang 
    # Step # | name | target | value
    # 1 | open | https://app.jubelio.com/login | 
    self.driver.get("https://app.jubelio.com/login")
    # 2 | setWindowSize | 976x1040 | 
    self.driver.set_window_size(976, 1040)
    # 3 | click | name=email | 
    self.driver.find_element(By.NAME, "email").click()
    # 4 | type | name=email | qa.rakamin.jubelio@gmail.com
    self.driver.find_element(By.NAME, "email").send_keys("qa.rakamin.jubelio@gmail.com")
    # 5 | click | name=password | 
    self.driver.find_element(By.NAME, "password").click()
    # 6 | type | name=password | Jubelio123!
    self.driver.find_element(By.NAME, "password").send_keys("Jubelio123!")
    # 7 | click | css=.ladda-button | 
    self.driver.find_element(By.CSS_SELECTOR, ".ladda-button").click()
    # 8 | mouseOver | css=.ladda-button | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".ladda-button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 9 | click | css=.metismenu-container:nth-child(1) > .metismenu-item:nth-child(2) > .metismenu-link > span:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".metismenu-container:nth-child(1) > .metismenu-item:nth-child(2) > .metismenu-link > span:nth-child(2)").click()
    # 10 | click | css=.visible > .metismenu-item:nth-child(2) span | 
    self.driver.find_element(By.CSS_SELECTOR, ".visible > .metismenu-item:nth-child(2) span").click()
    # 11 | click | linkText=Habis | 
    self.driver.find_element(By.LINK_TEXT, "Habis").click()
    # 12 | click | linkText=Menipis | 
    self.driver.find_element(By.LINK_TEXT, "Menipis").click()
    # 13 | click | linkText=Tidak Laku | 
    self.driver.find_element(By.LINK_TEXT, "Tidak Laku").click()
  
