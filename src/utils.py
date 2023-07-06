```python
import requests
from PIL import Image
import pytesseract
from io import BytesIO

class Utils:
    @staticmethod
    def process_image_question(image_url):
        """
        Process image containing question text.
        """
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        question_text = pytesseract.image_to_string(img)
        return question_text

    @staticmethod
    def validate_question(question):
        """
        Validate the user's question.
        """
        if not question:
            raise ValueError("Question cannot be empty.")
        if len(question) > 1000:
            raise ValueError("Question is too long.")
        return True

    @staticmethod
    def format_answer(answer):
        """
        Format the AI-generated answer.
        """
        return answer.strip()

    @staticmethod
    def evaluate_performance(correct_answers, total_questions):
        """
        Evaluate the performance of the extension.
        """
        accuracy = correct_answers / total_questions
        return accuracy
```