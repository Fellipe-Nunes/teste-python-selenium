import json
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ScreenshotManager:
    def __init__(self, screenshot_dir='screenshots'):
        self.screenshot_dir = screenshot_dir

        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def take_screenshot(self, driver, filename):
        screenshot_path = os.path.join(self.screenshot_dir, filename)
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")


class AutomationTest:
    def __init__(self, config_path):
        with open(config_path) as f:
            self.config = json.load(f)
        
        self.base_url = self.config.get('base_url', '')
        self.endpoint = self.config.get('endpoint', '')
        self.full_url = self.base_url + self.endpoint
        
        self.driver = webdriver.Chrome()  
        self.driver.maximize_window()
        self.screenshot_manager = ScreenshotManager()

    def test_register(self):
        self.driver.get(self.full_url)
        fields = self.config['fields']
        selectors = self.config['selectors']
        # Preencher campos do formulário
        for field, value in fields.items():
            if field == "Gender":
                gender_selector = selectors['gender_male_radio'] if value.lower() == "male" else selectors['gender_female_radio']
                self.driver.find_element_by_xpath(gender_selector).click()
            elif field == "Hobbies":
                for hobby in value:
                    hobby_checkbox = selectors['hobbies_' + hobby.lower() + '_checkbox']
                    self.driver.find_element_by_xpath(hobby_checkbox).click()
            elif field == "Languages":
                self.driver.find_element_by_xpath(selectors['languages_dropdown']).click()
                for language in value:
                    language_option = "//a[contains(text(),'" + language + "')]"
                    self.driver.find_element_by_xpath(language_option).click()
            elif field == "Date Of Birth":
                for subfield, subvalue in value.items():
                    subfield_selector = selectors[subfield.lower() + '_dropdown']
                    self.driver.find_element_by_xpath(subfield_selector).send_keys(subvalue)
            else:
                self.driver.find_element_by_xpath(selectors[field.lower() + '_input']).send_keys(value)
        self.driver.find_element_by_xpath(selectors['submit_button']).click()
        self.screenshot_manager.take_screenshot(self.driver, "register_test.png")

def test_frames(self):
    self.driver.get(self.full_url)
    frames_link_text = self.config.get('frames_link_text', '')
    frames_sublink_text = self.config.get('frames_sublink_text', '')

    self.driver.find_element_by_link_text(frames_link_text).click()
    self.driver.find_element_by_link_text(frames_sublink_text).click()

    self.driver.switch_to.frame("singleframe")
    frame_text = self.config.get('frame_text', '')
    frame_textbox = self.driver.find_element_by_xpath("//input[@type='text']")
    frame_textbox.send_keys(frame_text)
    self.screenshot_manager.take_screenshot(self.driver, "frames_test.png")

    def test_datepicker(self):
        self.driver.get(self.full_url)
        birthdate = self.config.get('birthdate', '')
        datepicker_ids = self.config.get('datepicker_ids', {})
        
        for datepicker_id in datepicker_ids.values():
            datepicker_field = self.driver.find_element_by_id(datepicker_id)
            datepicker_field.clear()
            datepicker_field.send_keys(birthdate)        
        self.screenshot_manager.take_screenshot(self.driver, "datepicker_test.png")

    def test_slider(self):
        self.driver.get(self.full_url)
        self.driver.find_element_by_link_text(self.config['widgets_link_text']).click()
        self.driver.find_element_by_link_text(self.config['slider_link_text']).click()
        slider_handle = self.driver.find_element_by_xpath(self.config['slider_handle_xpath'])
        slider_size = slider_handle.size['width']
        move = webdriver.ActionChains(self.driver)
        move.click_and_hold(slider_handle).move_by_offset(slider_size / 2, 0).release().perform()
        self.screenshot_manager.take_screenshot(self.driver, "slider_test.png")

    def run_tests(self):
        if "fields" in self.config:
            self.test_register()
        elif "frames_link_text" in self.config and "frames_sublink_text" in self.config:
            self.test_frames()
        elif "datepicker_ids" in self.config:
            self.test_datepicker()
        elif "slider_link_text" in self.config:
            self.test_slider()
        self.driver.quit()


if __name__ == "__main__":
    config_paths = ["configs/config_register.json", "configs/config_frames.json", "configs/config_datepicker.json",
                    "configs/config_slider.json"]
    for config_path in config_paths:
        test = AutomationTest(config_path)
        test.run_tests()
