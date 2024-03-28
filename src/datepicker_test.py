import json
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DatepickerTest(unittest.TestCase):
    def setUp(self):
        with open("configs/config_datepicker.json") as f:
            self.config = json.load(f)
        
        self.base_url = self.config.get('base_url', '')
        self.endpoint = self.config.get('endpoint', '')
        self.full_url = self.base_url + self.endpoint
        
        self.driver = webdriver.Chrome()  
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_datepicker(self):
        self.driver.get(self.full_url)
        birthdate = self.config.get('birthdate', '')
        datepicker_ids = self.config.get('datepicker_ids', {})
        
        for datepicker_id in datepicker_ids.values():
            datepicker_field = self.driver.find_element_by_id(datepicker_id)
            datepicker_field.clear()
            datepicker_field.send_keys(birthdate)

        # Add assertion here if needed

if __name__ == "__main__":
    unittest.main()
