import json
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SliderTest(unittest.TestCase):
    def setUp(self):
        with open("configs/config_slider.json") as f:
            self.config = json.load(f)
        
        self.base_url = self.config.get('base_url', '')
        self.endpoint = self.config.get('endpoint', '')
        self.full_url = self.base_url + self.endpoint
        
        self.driver = webdriver.Chrome()  
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_slider(self):
        self.driver.get(self.full_url)
        self.driver.find_element_by_link_text(self.config['widgets_link_text']).click()
        self.driver.find_element_by_link_text(self.config['slider_link_text']).click()
        slider_handle = self.driver.find_element_by_xpath(self.config['slider_handle_xpath'])
        slider_size = slider_handle.size['width']
        move = webdriver.ActionChains(self.driver)
        move.click_and_hold(slider_handle).move_by_offset(slider_size / 2, 0).release().perform()

        # Add assertion here if needed

if __name__ == "__main__":
    unittest.main()
