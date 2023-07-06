```python
import openai

class AIModelAccess:
    def __init__(self, api_key):
        self.api_key = api_key
        self.ai_model = None

    def accessAIModel(self):
        try:
            openai.api_key = self.api_key
            self.ai_model = openai.GPT3
            print("AI model accessed successfully.")
        except Exception as e:
            print(f"Failed to access AI model: {e}")
            return None

        return self.ai_model

    def getAIModel(self):
        if not self.ai_model:
            self.accessAIModel()
        return self.ai_model
```