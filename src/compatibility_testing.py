```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class CompatibilityTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_compatibility(self):
        driver = self.driver
        driver.get("http://localhost:8000")  # Assuming the extension is hosted locally
        question_input = driver.find_element(By.ID, "questionInput")
        submit_button = driver.find_element(By.ID, "submitQuestion")
        display_area = driver.find_element(By.ID, "displayAnswer")

        # Test question input
        question_input.send_keys("What is the capital of France?")
        submit_button.click()

        # Wait for the answer to be generated and displayed
        driver.implicitly_wait(10)  # wait for 10 seconds

        # Check if the answer is displayed
        self.assertIsNotNone(display_area.text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
```