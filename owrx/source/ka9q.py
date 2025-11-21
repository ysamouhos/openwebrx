from owrx.source.connector import ConnectorSource, ConnectorDeviceDescription
from owrx.command import Option, Flag
from owrx.form.input import Input, NumberInput, TextInput, CheckboxInput
from owrx.form.input.validator import RangeValidator, Range
from typing import List

class Ka9qSource(ConnectorSource):
    def getCommandMapper(self):
        return (
            super()
            .getCommandMapper()
            .setBase("pcmrecord")
            .setMappings(
                {
                    "tuner_freq": Option("-ssrc"),
                    "debug": Flag("--debug"),
                }
            )
        )


class RemoteInput(TextInput):
    def __init__(self):
        super().__init__(
            "remote",
            "Multicast IP",
            infotext=(
                "Multicast IP address of stream."
            )
        )


class Ka9qDeviceDescription(ConnectorDeviceDescription):
    def getName(self):
        return "KA9Q Radiod Streams"

    def getInputs(self) -> List[Input]:
        return super().getInputs() + [
            RemoteInput(),
            NumberInput(
                "tuner_freq",
                "SSRC",
                "SSRC is the name of the stream (no default)",
                validator=RangeValidator(0, 60)
            ),
            CheckboxInput(
                "debug",
                "Show connector debugging messages in the log"
            ),
        ]
