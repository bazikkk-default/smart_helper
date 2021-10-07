import pyttsx3
from typing import List, Tuple
from time import sleep


class Voice:

    def __init__(self, lang: str = 'ru', voice_name: str = 'Anna'):
        self.tts = pyttsx3.init()
        self.tts.setProperty('rate', self.tts.getProperty('rate') - 40)  # Скорость произношения
        self.tts.setProperty('volume', self.tts.getProperty('volume') + 0.9)  # Громкость голоса
        self.voices = self.tts.getProperty('voices')

        # Задать голос по умолчанию
        self.tts.setProperty('voice', lang)

        # Попробовать установить предпочтительный голос
        for voice in self.voices:
            if voice.name == voice_name:
                self.tts.setProperty('voice', voice.id)

    @classmethod
    def say(cls, text: str):
        instance = cls()
        instance.tts.say(text)
        instance.tts.runAndWait()

    def speak(self, array: List[Tuple[str, int]]):
        for row in array:
            text, wait = row
            self.tts.say(text)
            self.tts.runAndWait()
            sleep(wait or 0)
