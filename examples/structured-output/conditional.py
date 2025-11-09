from utils.openai_client import get_response

text = "Como estas hoy? Espero que todo vaya bien. Estoy aprendiendo a programar en Python y me encanta."

prompt = f"""
You will be provided with a text delimited by triple backticks. If the text is written in English, suggest as suitable title for it. Otherwise, write 'I only understand English.'.
```{text}```
"""

print(get_response(prompt))

# Output:
# I only understand English.
