```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from src import extension_main

class CompatibilityTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_compatibility_firefox(self):
        driver = self.driver
        driver.get("http://localhost:8000")
        self.assertIn("Question Answering Extension", driver.title)
        questionInput = driver.find_element_by_id("questionInput")
        submitQuestion = driver.find_element_by_id("submitQuestion")
        displayAnswer = driver.find_element_by_id("displayAnswer")

        questionInput.send_keys("What is the capital of France?")
        submitQuestion.click()
        self.assertTrue(displayAnswer.text, "Paris")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
```
This is a basic compatibility test for the Firefox browser. It uses Selenium WebDriver for browser automation. The test navigates to the extension's page, inputs a question, submits it, and checks if the answer is displayed correctly. Similar tests can be written for other browsers like Chrome, Safari, etc.