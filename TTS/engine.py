import re
import pyttsx3

class TTS_Engine:
  def __init__(self, volume, rate):
    self.engine = pyttsx3.init()
    self.volume = volume
    self.rate = rate
    self.voices = self.engine.getProperty("voices")

  def clean_text(self, text: str) -> str:
    text = re.sub(r"[^\w\s.,!?'-]", "", text)
    return text

  def speak(self, text: str) -> None:
    self.engine.setProperty("rate", self.rate)
    self.engine.setProperty("volume", self.volume)
    self.engine.setProperty("voice", self.voices[1].id)
    clea_text = self.clean_text(text)
    self.engine.say(clea_text)
    self.engine.runAndWait()