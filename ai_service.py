import requests
from prompts import TECHNICAL_PROMPT

def ask_ollama(prompt):

    full_prompt = TECHNICAL_PROMPT + "\n\nUser message: \n" + prompt

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": full_prompt,
            "stream": False
        }
    )
    data = response.json()
    print("The response of ask_ollama is: ", data)
    
    return data.get("response", "No response was generated, try again later or contact Admin.") 
