from TTS.engine import TTS_Engine
from LLM.client import Client

client = Client()
voice = TTS_Engine(1.0, 175)

def wait_for_input():
    entry = input("entry: ")
    return entry

def wait_for_respound(entry):
    respound = client.respound(entry)
    return respound
    
def run():
    while True:
        entry = wait_for_input()
        if entry.lower() == "exit":
            break
        
        respound = wait_for_respound(entry)
        print(respound)
        
        voice.speak(respound)

        
