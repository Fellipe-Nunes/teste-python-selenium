import json
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FrameTest(unittest.TestCase):
    def setUp(self):
        with open("configs/config_frames.json") as f:
            self.config = json.load(f)
        
        self.base_url = self.config.get('base_url', '')
        self.endpoint = self.config.get('endpoint', '')
        self.full_url = self.base_url + self.endpoint
        
        self.driver = webdriver.Chrome()  
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_frame(self):
        self.driver.get(self.full_url)
        frames_link_text = self.config.get('frames_link_text', '')
        frames_sublink_text = self.config.get('frames_sublink_text', '')

        self.driver.find_element_by_link_text(frames_link_text).click()
        self.driver.find_element_by_link_text(frames_sublink_text).click()

        self.driver.switch_to.frame("singleframe")
        frame_text = self.config.get('frame_text', '')
        frame_textbox = self.driver.find_element_by_xpath("//input[@type='text']")
        frame_textbox.send_keys(frame_text)

        # Add assertion here if needed

if __name__ == "__main__":
    unittest.main()
