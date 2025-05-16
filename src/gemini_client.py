"""
Module for interacting with the Gemini API.
"""
import google.generativeai as genai

class GeminiClient:
    """Client for interacting with the Gemini API."""

    def __init__(self, api_key):
        """
        Initialize the Gemini client.

        Args:
            api_key (str): The API key for the Gemini API.
        """
        self.api_key = api_key
        genai.configure(api_key=api_key)

        # Configure the model - specifically use Gemini 2.0 Flash
        try:
            # List available models to check if Gemini 2.0 Flash is available
            models = genai.list_models()
            available_models = [model.name for model in models]

            # Look for Gemini 2.0 Flash models
            gemini_2_flash_models = [m for m in available_models if "gemini-2.0-flash" in m and "vision" not in m.lower()]

            if gemini_2_flash_models:
                # Use the first Gemini 2.0 Flash model found
                model_name = gemini_2_flash_models[0]
                self.model = genai.GenerativeModel(model_name)
                print(f"Using Gemini 2.0 Flash model: {model_name}")
            else:
                # If Gemini 2.0 Flash is not available, use the default model name
                model_name = 'models/gemini-2.0-flash'
                self.model = genai.GenerativeModel(model_name)
                print(f"Using default Gemini 2.0 Flash model: {model_name}")
        except Exception as e:
            print(f"Error configuring model: {e}")
            # Fallback to Gemini 2.0 Flash
            self.model = genai.GenerativeModel('models/gemini-2.0-flash')
            print("Using fallback Gemini 2.0 Flash model")

    def generate_text(self, prompt):
        """
        Generate text using the Gemini API.

        Args:
            prompt (str): The prompt to send to the API.

        Returns:
            str: The generated text.
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error generating text: {e}")
            return f"Error: {str(e)}"

    def check_connection(self):
        """
        Check if the connection to the Gemini API is working.

        Returns:
            bool: True if the connection is working, False otherwise.
        """
        try:
            response = self.model.generate_content("Hello, are you working?")
            return True if response.text else False
        except Exception as e:
            print(f"Connection error: {e}")
            return False
