from core.primitives import Emitter, EMField, SignalEvent, SignalMessage
from core.signal_model import SignalFrame
from core.time_frequency_frame import TimeFrequencyFrame
from typing import Dict, List

# make this a decorator and use it instead
def filter_by_time_range(filterable, start: float, end: float) -> List:
    return [f for f in filterable if start <= f.timestamp <= end]

# add methods in 5/7 collections doc.

class SignalFrameArray:

    def __init__(self, frames: List[SignalFrame]):
        self.frames = frames

    def select_range(self, start: float, end: float) -> List[SignalFrame]:
        return [f for f in self.frames if start <= f.timestamp <= end]

    def filter_by_time_range(self, start: float, end: float) -> List[SignalFrame]:
        return filter_by_time_range(self.frames, start, end)


class TimeFrequencyFrameList:

    def __init__(self, frames: List[TimeFrequencyFrame]):
        self.frames = frames

    def select_range(self, start: float, end: float) -> List[TimeFrequencyFrame]:
        return [f for f in self.frames if start <= f.start_time <= end]

    def filter_by_time_range(self, start: float, end: float) -> List[TimeFrequencyFrame]:
        return filter_by_time_range(self.frames, start, end)


class EmitterGroup:

    def __init__(self, emitters: Dict[str, Emitter]):
        self.emitters = emitters

    def get_emitter(self, _id):
        return self.emitters[_id]

    def get_emitters_by_platform_type(self, platform_type):
        return [self.emitters[id] for id in self.emitters if self.emitters[id].platform_type is platform_type]

    # Bias dict comparison
    # Bias dict merge
    # search description field in a collection
    # get list of id
    # get list of description


class EMFieldArray:

    def __init__(self, fields: List[EMField]):
        self.fields = fields

    def filter_by_time_range(self, start: float, end: float) -> List[EMField]:
        return filter_by_time_range(self.fields, start, end)


class SignalEventList:

    def __init__(self, events: List[SignalEvent]):
        self.events = events

    def filter_by_time_range(self, start: float, end: float) -> List[SignalEvent]:
        return filter_by_time_range(self.events, start, end)


class SignalMessageList:

    def __init__(self, frames: List[SignalMessage]):
        self.frames = frames

    def filter_by_time_range(self, start: float, end: float) -> List[SignalMessage]:
        return filter_by_time_range(self.frames, start, end)

