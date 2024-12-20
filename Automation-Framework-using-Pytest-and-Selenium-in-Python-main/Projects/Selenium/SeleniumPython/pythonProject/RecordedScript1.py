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


class TestMySuite1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_myTEST2(self):
        self.driver.get("https://trytestingthis.netlify.app/index.html")
        self.driver.set_window_size(965, 520)
        self.driver.find_element(By.ID, "fname").click()
        self.driver.find_element(By.ID, "fname").click()
        self.driver.find_element(By.ID, "fname").send_keys("iffath")
        self.driver.find_element(By.ID, "lname").click()
        self.driver.find_element(By.ID, "lname").send_keys("khan")
        self.driver.find_element(By.CSS_SELECTOR, "label:nth-child(17)").click()
        self.driver.find_element(By.ID, "option").click()
        dropdown = self.driver.find_element(By.ID, "option")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 2']").click()
        dropdown = self.driver.find_element(By.ID, "owc")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 1']").click()
        dropdown = self.driver.find_element(By.ID, "owc")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 1']").click()
        dropdown = self.driver.find_element(By.ID, "owc")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 2']").click()
        self.driver.find_element(By.CSS_SELECTOR, "#owc > option:nth-child(3)").click()
        self.driver.find_element(By.ID, "moption").click()
        self.driver.find_element(By.NAME, "option2").click()
        self.driver.find_element(By.NAME, "option3").click()
        self.driver.find_element(By.NAME, "Options").click()
        self.driver.find_element(By.NAME, "Options").send_keys("Strawberry")
        self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(1)").click()
        self.driver.find_element(By.ID, "favcolor").click()
        self.driver.find_element(By.ID, "favcolor").send_keys("#d33c70")
        self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(1)").click()
        self.driver.find_element(By.ID, "day").click()
        self.driver.find_element(By.ID, "day").send_keys("2024-07-13")
        element = self.driver.find_element(By.ID, "a")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "a")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "a")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "a").send_keys("100")
        self.driver.find_element(By.ID, "a").click()
        self.driver.find_element(By.ID, "quantity").click()
        self.driver.find_element(By.ID, "quantity").send_keys("5")
        self.driver.find_element(By.NAME, "message").click()
        self.driver.find_element(By.NAME, "message").send_keys("The cat was playing in the garden.\\nOK welldone")
        element = self.driver.find_element(By.ID, "owc")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "owc")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "owc")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(1)").click()
        element = self.driver.find_element(By.ID, "owc")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "owc")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "owc")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(1)").click()
        self.driver.find_element(By.NAME, "message").click()
        self.driver.find_element(By.NAME, "message").click()
        self.driver.find_element(By.NAME, "message").send_keys("The cat was playing in the garden.\\nOK well done")
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".btn")
        assert len(elements) > 0
        self.driver.find_element(By.ID, "uname").click()
        self.driver.find_element(By.ID, "uname").send_keys("test")
        self.driver.find_element(By.ID, "uname").send_keys(Keys.DOWN)
        self.driver.find_element(By.ID, "uname").send_keys(Keys.DOWN)
        self.driver.find_element(By.ID, "uname").send_keys("test")
        self.driver.find_element(By.ID, "pwd").click()
        self.driver.find_element(By.ID, "pwd").send_keys("test")
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(10)").click()
        self.driver.find_element(By.CSS_SELECTOR, "h2").click()
        self.driver.find_element(By.CSS_SELECTOR, "h2").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, "h2")
        assert len(elements) > 0

