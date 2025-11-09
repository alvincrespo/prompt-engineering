from utils.openai_client import get_response

text = "I bought your XYZ Smart Watch and wanted to share my positive experience. Impressed with it's sleek design, comfort, and touchscreen usability."

prompt = f"""
Identify emotions used in this text. Don't use more than 3 emotions.
Format your answer as a list of words separated by commas:
```{text}```
"""

print(get_response(prompt))

# Output:
# positive, impressed, satisfaction
