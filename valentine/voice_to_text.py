import speech_recognition as sr
import logging
import whisper
import torch
import numpy as np


logger = logging.getLogger('sLogger')


class VoiceToText:

    def __init__(self, sample_rate=-1):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone(sample_rate=sample_rate)
        logger.debug("recorder: loading model tiny.en")
        self.model = whisper.load_model("tiny.en")
        logger.debug("recorder: finish loading model tiny.en")

    def get(self):
        with self.mic as source:
            logger.debug("recorder: listening")
            audio = self.r.listen(source)
        logger.debug("recorder: end listening")
        logger.debug("recorder: torch audio data")
        audio_data = torch.from_numpy(np.frombuffer(audio.get_raw_data(), np.int16).flatten().astype(np.float32) / 32768.0)
        logger.debug("recorder: transcribe")
        result = self.model.transcribe(audio_data, language='english', fp16=False)
        return result['text']
