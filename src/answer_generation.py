```python
import openai
from src.ai_model_access import accessAIModel
from src.utils import QuestionSchema

def generateAnswer(user_question):
    # Access the AI model
    ai_model = accessAIModel()

    # Ensure the question is in the correct format
    if not isinstance(user_question, QuestionSchema):
        raise ValueError("Invalid question format. Please use the QuestionSchema format.")

    # Generate the answer using the AI model
    response = ai_model.Completion.create(
        engine="text-davinci-002",
        prompt=user_question.text,
        temperature=0.5,
        max_tokens=100
    )

    # Extract the generated answer from the response
    generated_answer = response.choices[0].text.strip()

    return generated_answer
```