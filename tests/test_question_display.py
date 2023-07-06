```python
import unittest
from src import question_display

class TestQuestionDisplay(unittest.TestCase):

    def setUp(self):
        self.question_display = question_display.displayQuestion()

    def test_display_question(self):
        user_question = "What is the capital of France?"
        self.question_display.display(user_question)
        self.assertEqual(self.question_display.question, user_question)

    def test_clear_question(self):
        user_question = "What is the capital of France?"
        self.question_display.display(user_question)
        self.question_display.clear()
        self.assertEqual(self.question_display.question, "")

if __name__ == '__main__':
    unittest.main()
```