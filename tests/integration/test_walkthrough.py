# Generated by Selenium IDE
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

class TestWalkthrough():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_walkthrough(self):
    self.driver.get("http://localhost:5000/login?next=%2F")
    self.driver.set_window_size(1440, 790)
    self.driver.find_element(By.CSS_SELECTOR, ".tablinks:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#Register #username").click()
    self.driver.find_element(By.CSS_SELECTOR, "#Register #username").send_keys("admin")
    self.driver.find_element(By.CSS_SELECTOR, "#Register #password").send_keys("admin")
    self.driver.find_element(By.ID, "confirm_password").send_keys("admin")
    self.driver.find_element(By.CSS_SELECTOR, "#Register p:nth-child(5)").click()
    self.driver.find_element(By.ID, "is_admin").click()
    self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(6) > #submit").click()
    self.driver.find_element(By.LINK_TEXT, "Content").click()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("admin")
    self.driver.find_element(By.ID, "password").send_keys("admin")
    self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(4) > label:nth-child(2)").click()
    self.driver.find_element(By.ID, "submit").click()
    self.driver.find_element(By.LINK_TEXT, "Content").click()
    self.driver.find_element(By.CSS_SELECTOR, ".openbtn").click()
    self.driver.find_element(By.ID, "content").click()
    self.driver.find_element(By.LINK_TEXT, "Assessments").click()
    self.driver.find_element(By.LINK_TEXT, "Create Assessment").click()
    self.driver.find_element(By.ID, "question").click()
    self.driver.find_element(By.ID, "question").send_keys("assessment")
    self.driver.find_element(By.ID, "answer").send_keys("123")
    self.driver.find_element(By.ID, "submit").click()
    self.driver.find_element(By.LINK_TEXT, "Assessments").click()
    self.driver.find_element(By.LINK_TEXT, "Assessment 1").click()
    self.driver.find_element(By.ID, "answer").click()
    self.driver.find_element(By.ID, "answer").send_keys("123")
    self.driver.find_element(By.ID, "submit").click()
    self.driver.find_element(By.LINK_TEXT, "Manage Assessments").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.LINK_TEXT, "Profile").click()
    self.driver.find_element(By.LINK_TEXT, "Edit Profile").click()
    self.driver.find_element(By.ID, "description").click()
    self.driver.find_element(By.ID, "description").send_keys("desc")
    self.driver.find_element(By.CSS_SELECTOR, ".grey_box:nth-child(3)").click()
    self.driver.find_element(By.ID, "submit").click()
  
