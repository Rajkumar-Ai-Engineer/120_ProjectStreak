import requests 

response = requests.post("http://localhost:8000/pokemon_assistant/invoke",
                         json={"input":{"question":"God of Pokemon overall"}})

print(response.json())