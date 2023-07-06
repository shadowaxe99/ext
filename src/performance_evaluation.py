```python
import time
from src.ai_model_access import accessAIModel
from src.answer_generation import generateAnswer
from src.question_submission import submitQuestion

class PerformanceEvaluation:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.ai_model = accessAIModel()

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        self.end_time = time.time()

    def get_processing_time(self):
        return self.end_time - self.start_time

    def evaluate_performance(self, user_question, correct_answer):
        self.start_timer()
        submitted_question = submitQuestion(user_question)
        generated_answer = generateAnswer(self.ai_model, submitted_question)
        self.stop_timer()

        processing_time = self.get_processing_time()
        answer_accuracy = self.evaluate_answer_accuracy(generated_answer, correct_answer)

        return {
            "processing_time": processing_time,
            "answer_accuracy": answer_accuracy
        }

    def evaluate_answer_accuracy(self, generated_answer, correct_answer):
        if generated_answer == correct_answer:
            return 1
        else:
            return 0
```