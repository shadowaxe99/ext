```python
from src.utils import QuestionSchema
from src.ai_model_access import accessAIModel

def submitQuestion(user_question):
    """
    Function to submit the user's question for processing.
    """
    # Validate the user's question using the QuestionSchema
    if not QuestionSchema.validate(user_question):
        raise ValueError("Invalid question format. Please submit a valid question.")

    # Access the AI model
    ai_model = accessAIModel()

    # Submit the question to the AI model for processing
    ai_model.submit_question(user_question)

    return True
```