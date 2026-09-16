from TTS.engine import TTS_Engine
from LLM.client import Client

client = Client()
entry = input("entry: ")
respound = client.respound(entry)
print(respound)

voice = TTS_Engine(1.0, 175)
voice.speak(respound)