from pycsdr.modules import ExecModule
from pycsdr.types import Format


class StreamerModule(ExecModule):
    def __init__(self, sampleRate: int = 36000):
        cmd = ["streamer"]
        super().__init__(Format.COMPLEX_FLOAT, Format.CHAR, cmd)

