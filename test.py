import os
print("API KEY:", os.environ.get("OPENAI_API_KEY"))  # None なら読み込めていない