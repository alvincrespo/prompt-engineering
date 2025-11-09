from utils.openai_client import get_response

text = "Dear sir, I wanted too discus a potentiel opporuntiy for colaboration. Pls let me know wen you're avialable."

prompt = f"""
Proofread the text delimited by triple backticks while keeping the original text structure intact:
```{text}```
"""

print(get_response(prompt))

# Output:
# Dear sir, I wanted to discuss a potential opportunity for collaboration. Please let me know when you're available.
