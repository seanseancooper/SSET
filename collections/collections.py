from core.primitives import Emitter, EMField, SignalEvent, SignalMessage
from core.signal_model import SignalFrame
from core.time_frequency_frame import TimeFrequencyFrame
from typing import Dict, List, Generic, T


class SignalCollection(Generic[T]):
    def __init__(self, items: List[T]):
        self.items = items

    # add methods in 5/7 collections doc.

    def filter_by_time(self, start: float, end: float) -> List[T]:
        return [i for i in self.items if start <= i.timestamp <= end]

    def sort_by_time(self):
        self.items.sort(key=lambda x: x.timestamp)


class SignalFrameArray(SignalCollection):

    def __init__(self, frames: List[SignalFrame], items: List[T]):
        super().__init__(items)
        self.frames = frames

    def select_range(self, start: float, end: float) -> List[SignalFrame]:
        return [f for f in self.frames if start <= f.timestamp <= end]


class TimeFrequencyFrameList(SignalCollection):

    def __init__(self, frames: List[TimeFrequencyFrame], items: List[T]):
        super().__init__(items)
        self.frames = frames

    def select_range(self, start: float, end: float) -> List[TimeFrequencyFrame]:
        return [f for f in self.frames if start <= f.start_time <= end]


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


class EMFieldArray(SignalCollection):

    def __init__(self, fields: List[EMField], items: List[T]):
        super().__init__(items)
        self.fields = fields


class SignalEventList(SignalCollection):

    def __init__(self, events: List[SignalEvent], items: List[T]):
        super().__init__(items)
        self.events = events


class SignalMessageList(SignalCollection):

    def __init__(self, frames: List[SignalMessage], items: List[T]):
        super().__init__(items)
        self.frames = frames
