import requests
from .Personality import PERSONALITY

entry = None
respond = None
API = ""

class Client:
  def __init__(self):
    pass

  def respound(self, entry):
    URL = API
    data = {
        "messages": [
            {
              "role": "system",
              "content": PERSONALITY
            },
            {
              "role": "user",
              "content": entry
            }
        ]
    }
    response = requests.post(URL, json=data)
    return response.json()['response']
  