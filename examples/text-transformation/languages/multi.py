from utils.openai_client import get_response

text = "The product combines top quality with a fair price."

prompt = f"""
Translate the English text delimited by triple backticks to French, Spanish and German:
```{text}```
"""

print(get_response(prompt))

# Output:
# Here are the translations:

# **French:** Le produit allie une qualité supérieure à un prix équitable.

# **Spanish:** El producto combina alta calidad con un precio justo.

# **German:** Das Produkt vereint hohe Qualität mit einem fairen Preis.
