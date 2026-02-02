from csdr.chain.demodulator import ServiceDemodulator, DialFrequencyReceiver
from csdr.module.streamer import StreamerModule

class StreamerDemodulator(ServiceDemodulator):
    def __init__(self, sampleRate: int = 36000, service: bool = False):
        self.sampleRate = sampleRate
        workers = [ StreamerModule(sampleRate) ]
        super().__init__(workers)

    def supportsSquelch(self) -> bool:
        return False

    def getFixedAudioRate(self) -> int:
        return self.sampleRate

