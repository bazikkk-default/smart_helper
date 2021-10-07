from vosk import Model, KaldiRecognizer
import pyaudio
import math
import struct
import time
from json import loads
from voice.main import Voice
from .task_array import Loop


class Recorder:

    def rms(self, frame):
        shorts = struct.unpack("%dh" % (len(frame) / self.swidth), frame)
        sum_squares = 0.0
        for sample in shorts:
            n = sample * self.short_norm
            sum_squares += n * n
        rms = math.pow(sum_squares / len(frame) / self.swidth, 0.5)

        return rms * 1000

    def __init__(self):
        self.Threshold = 10
        self.short_norm = (1.0 / 32768.0)
        self.chunk = 1024
        self.swidth = 2
        self.model = Model("vosk-model-small-ru-0.15")
        self.rec = KaldiRecognizer(self.model, 16000)
        self.p = pyaudio.PyAudio()
        self.loop = Loop()
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, output=True,
                                  frames_per_buffer=self.chunk)

    def record(self):
        rec = []
        current = time.time()
        end = time.time() + 3   # TIMEOUT

        while current <= end:

            data = self.stream.read(self.chunk)
            if self.rms(data) >= self.Threshold:
                end = time.time() + 3  # TIMEOUT

            current = time.time()
            rec.append(data)
        self.write(b''.join(rec))

    def write(self, recording):
        if self.rec.AcceptWaveform(recording):
            text = loads(self.rec.Result()).get('text')
            if self.loop.check_clear():
                self.loop.create_task(text)
            else:
                self.loop.answer(text)
            print(text)

    def listen(self):
        Voice.say('Привет я мразь')

        while True:
            input = self.stream.read(self.chunk)
            rms_val = self.rms(input)
            if rms_val > self.Threshold:
                self.record()

