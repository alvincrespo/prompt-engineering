from utils.openai_client import get_response

text = """
The XYZ Mobile X200: a sleek 6.5-inch Super AMOLED smartphone with a 48MP
triple-camera, octa-core processor, 5000mAh battery, 5G connectivity, and Android 11 OS.
Secure with fingerprint and facial recognition. 128GB storage, expandable up to 512GB.
"""

prompt = f"""
Identify the following entities from the text delimited by triple backticks:
- Product Name
- Display Size
- Camera Resolution
Format the answer as an unordered list.
```{text}```
"""

print(get_response(prompt))

# Output:
# - Product Name: XYZ Mobile X200
# - Display Size: 6.5-inch
# - Camera Resolution: 48MP
