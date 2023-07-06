```python
import unittest
from unittest.mock import patch
from src import ai_model_access

class TestAIModelAccess(unittest.TestCase):

    @patch('src.ai_model_access.openai.GPT3')
    def test_access_ai_model(self, mock_gpt3):
        # Mock the GPT-3 model
        mock_gpt3.return_value = 'mocked_model'

        # Call the function to access the AI model
        result = ai_model_access.accessAIModel()

        # Assert that the function returns the mocked model
        self.assertEqual(result, 'mocked_model')

        # Assert that the GPT-3 model was accessed
        mock_gpt3.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```