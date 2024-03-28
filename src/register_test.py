import json
import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://demo.automationtesting.in"
        self.endpoint = "/Register.html"
        self.full_url = self.base_url + self.endpoint
        
        self.driver = webdriver.Chrome()  
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        self.driver.get(self.full_url)
        
        # Campos do formulário
        fields = {
            "First Name": "Fellipe",
            "Last Name": "Nunes",
            "Address": "rua python, 123",
            "Email address": "fellipe@exemplo.com",
            "Phone": "1234567890",
            "Gender": "Male",
            "Hobbies": ["Cricket"],
            "Languages": ["English"],
            "Skills": "Python",
            "Country": "Brazil",
            "Date Of Birth": {
                "year": "1988",
                "month": "March",
                "day": "23"
            },
            "Password": "Admin123",
            "Confirm Password": "Admin123"
        }
        
        # Seletores dos campos
        selectors = {
            "gender_male_radio": "input[value='Male']",
            "hobbies_cricket_checkbox": "input[value='Cricket']",
            "languages_dropdown": "#msdd",
            "submit_button": "#submitbtn"
        }
        
        wait = WebDriverWait(self.driver, 30)  # Definindo um timeout

        # Preencher campos do formulário
        for field, value in fields.items():
            if field == "Gender":
                gender_selector = selectors['gender_male_radio'] if value.lower() == "male" else selectors['gender_female_radio']
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, gender_selector))).click()
            elif field == "Hobbies":
                for hobby in value:
                    hobby_checkbox = selectors['hobbies_' + hobby.lower() + '_checkbox']
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, hobby_checkbox))).click()
            elif field == "Languages":
                self.driver.find_element(By.CSS_SELECTOR, selectors['languages_dropdown']).click()
                for language in value:
                    language_option = "a:contains('" + language + "')"
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, language_option))).click()
            elif field == "Date Of Birth":
                for subfield, subvalue in value.items():
                    subfield_selector = "select#" + subfield.lower()
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, subfield_selector))).send_keys(subvalue)
            else:
                field_input = selectors.get(field.lower().replace(" ", "_") + '_input', '')  # Corrigindo acesso à chave
                if field_input:
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, field_input))).send_keys(value)
                else:
                    print(f"Campo não encontrado: {field}")
        
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['submit_button']))).click()

if __name__ == "__main__":
    unittest.main()
