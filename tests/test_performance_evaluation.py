```python
import unittest
from src import performance_evaluation

class TestPerformanceEvaluation(unittest.TestCase):

    def setUp(self):
        self.question = "What is the capital of France?"
        self.correct_answer = "Paris"

    def test_question_processing_time(self):
        start_time = time.time()
        performance_evaluation.submitQuestion(self.question)
        end_time = time.time()
        processing_time = end_time - start_time
        self.assertTrue(processing_time < 2)  # Assuming the acceptable processing time is less than 2 seconds

    def test_answer_accuracy(self):
        generated_answer = performance_evaluation.generateAnswer(self.question)
        self.assertEqual(generated_answer, self.correct_answer)

if __name__ == '__main__':
    unittest.main()
```