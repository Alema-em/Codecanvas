import requests
import re

def explain_code(code):

    prompt = f"""
Explain this Python code clearly.

Structure the answer using these sections:

What the program does
How the loop works
What the output will be

Code:
{code}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    explanation = data["response"]

    
    explanation = re.sub(r"\*\*(.*?)\*\*", r"<h3>\1</h3>", explanation)

    #
    explanation = explanation.replace("\n", "<br>")

    return explanation

