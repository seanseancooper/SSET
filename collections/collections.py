from core.primitives import Emitter, EMField, SignalEvent, SignalMessage
from core.signal_model import SignalFrame
from core.time_frequency_frame import TimeFrequencyFrame
from typing import Dict, List



class SignalFrameArray:

    def __init__(self, frames: List[SignalFrame]):
        self.frames = frames

    # query helpers
    def select_range(self, start: float, end: float) -> List[SignalFrame]:
        return [f for f in self.frames if start <= f.timestamp <= end]

    def filter_by_time_range(self, start: float, end: float) -> List[SignalFrame]:
        return [f for f in self.frames if start <= f.timestamp <= end]



class TimeFrequencyFrameList:

    def __init__(self, frames: List[TimeFrequencyFrame]):
        self.frames = frames

    def select_range(self, start: float, end: float) -> List[TimeFrequencyFrame]:
        return [f for f in self.frames if start <= f.start_time <= end]

    def filter_by_time_range(self, start: float, end: float) -> List[TimeFrequencyFrame]:
        return [f for f in self.frames if start <= f.start_time <= end]


class EmitterGroup:

    def __init__(self, emitters: Dict[str, Emitter]):
        self.emitters = emitters

    # Lookup by ID
    def get_emitter(self, _id):
        return self.emitters[_id]

    # Grouping by platform_type
    def get_emitters_by_platform_type(self, _platform):
        return [self.emitters[id] for id in self.emitters if self.emitters[id].platform_type is _platform]

    # Bias comparison or merge


class EMFieldArray:

    def __init__(self, fields: List[EMField]):
        self.fields = fields

    def filter_by_time_range(self, start: float, end: float) -> List[EMField]:
        return [f for f in self.fields if start <= f.timestamp <= end]


class SignalEventList:

    def __init__(self, events: List[SignalEvent]):
        self.events = events
        self.carrier_freq = events

    def filter_by_time(self, start: float, end: float) -> List[SignalEvent]:
        return [e for e in self.events if start <= e.timestamp <= end]

    def __eq__(self, other):
        return (super().__eq__(other) and
                self.carrier_freq == other.carrier_freq)


class SignalMessageList:

    def __init__(self, frames: List[SignalMessage]):
        self.frames = frames

    def filter_by_time_range(self, start: float, end: float) -> List[SignalMessage]:
        return [f for f in self.frames if start <= f.timestamp <= end]

