# app/llm/gemini.py

import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

class GeminiLLM:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-pro")

    def generate(self, prompt: str):
        response = self.model.generate_content(prompt)
        return response.text