# app/config.py

import os

GEMINI_API_KEY = os.getenv("AIzaSyDFzOnpee6vnu57TGbx28wamZtSWG8qob4")

LANGCHAIN_TRACING_V2 = "true"
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")