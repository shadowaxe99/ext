```python
from typing import Union
from PIL import Image
from io import BytesIO
import base64

class QuestionSchema:
    def __init__(self, text: str = None, image: Union[Image.Image, str] = None):
        self.text = text
        self.image = image

    def set_text(self, text: str):
        self.text = text

    def set_image(self, image: Union[Image.Image, str]):
        if isinstance(image, str):
            self.image = Image.open(BytesIO(base64.b64decode(image)))
        else:
            self.image = image

    def get_text(self):
        return self.text

    def get_image(self):
        return self.image

def displayQuestion(question: QuestionSchema):
    print(f"Question: {question.get_text()}")
    if question.get_image() is not None:
        question.get_image().show()
```