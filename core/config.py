"""
Configuration and constants for AI Dev Platform.
"""

import os

AI_PROVIDER_KEY = os.getenv("AI_PROVIDER_KEY", "your_api_key_here")

SUPPORTED_LANGUAGES = ["python", "javascript", "c", "cpp"]
