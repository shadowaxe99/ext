```python
from src.utils import AnswerSchema

def displayAnswer(generated_answer):
    """
    Function to display the generated answer.
    """
    # Validate the answer format
    if not isinstance(generated_answer, AnswerSchema):
        raise ValueError("Invalid answer format")

    # Display the answer in the extension's interface
    print(f"Answer: {generated_answer.text}")

    # If the answer includes an image, display it
    if generated_answer.image:
        print(f"Image: {generated_answer.image}")

    # If the answer includes a link, display it
    if generated_answer.link:
        print(f"Link: {generated_answer.link}")

    # If the answer includes additional information, display it
    if generated_answer.additional_info:
        print(f"Additional Information: {generated_answer.additional_info}")
```