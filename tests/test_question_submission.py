```python
import unittest
from src import question_submission

class TestQuestionSubmission(unittest.TestCase):

    def setUp(self):
        self.question_submission = question_submission.QuestionSubmission()

    def test_submit_text_question(self):
        user_question = "What is the capital of France?"
        self.question_submission.submitQuestion(user_question, "text")
        self.assertEqual(self.question_submission.user_question, user_question)

    def test_submit_image_question(self):
        user_question = "path/to/image.png"
        self.question_submission.submitQuestion(user_question, "image")
        self.assertEqual(self.question_submission.user_question, user_question)

    def test_invalid_question_type(self):
        user_question = "What is the capital of France?"
        with self.assertRaises(ValueError):
            self.question_submission.submitQuestion(user_question, "audio")

if __name__ == '__main__':
    unittest.main()
```