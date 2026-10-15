from faster_whisper import WhisperModel

class STT_Engine:
  def __init__(self):
    self.model = WhisperModel("base.en", device="cpu", compute_type="int8")

  def transcribe(self, audio_path: str) -> str:
    segments, info = self.model.transcribe(audio_path, beam_size=5)
    text = "".join(segments.text for segment in segments)
    return text.strip()


