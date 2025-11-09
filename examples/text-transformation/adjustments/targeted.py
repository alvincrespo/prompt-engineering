from utils.openai_client import get_response

text = "Our cutting-edge widget employs state-of-the-art microprocessors and advanced algorithms, delivering unparalleled efficiency and performance for a wide range of applicaitons."

prompt = f"""
Write the text delimited by triple backticks to be suitable for a non-technical audience:
```{text}```
"""

print(get_response(prompt))

# Output:
# Our innovative device uses the latest technology to work faster and more effectively than ever before, making it perfect for many different uses.
