```python
import unittest
from src import answer_generation

class TestAnswerGeneration(unittest.TestCase):

    def setUp(self):
        self.ai_model = answer_generation.ai_model
        self.user_question = "What is the capital of France?"
        self.expected_answer = "The capital of France is Paris."

    def test_generate_answer(self):
        generated_answer = answer_generation.generateAnswer(self.user_question)
        self.assertEqual(generated_answer, self.expected_answer)

    def test_answer_accuracy(self):
        accuracy = answer_generation.evaluatePerformance(self.user_question, self.expected_answer)
        self.assertTrue(accuracy > 0.8)

if __name__ == '__main__':
    unittest.main()
```