from core.primitives import Emitter, EMField, SignalEvent, SignalMessage
from core.signal_model import SignalFrame
from core.time_frequency_frame import TimeFrequencyFrame
from typing import Optional, Generic, T, Dict, List, Any, Tuple, Union


class SignalCollection(Generic[T]):
    def __init__(self, items: List[T]):
        self.items = items

    def filter_by_time(self, start: float, end: float) -> List[T]:
        return [i for i in self.items if start <= i.timestamp <= end]

    def sort_by_time(self):
        self.items.sort(key=lambda x: x.timestamp)


class SignalFrameArray(SignalCollection):
    # transform according to a function

    def __init__(self, items: List[SignalFrame]):
        super().__init__(items)

    def select_range(self, start: float, end: float) -> List[SignalFrame]:
        return [f for f in self.items if start <= f.timestamp <= end]

    def group_to_time_domain(self):
        return SignalFrameArray([frame.to_time_domain() for frame in self.items if frame.domain == "frequency"])

    def group_to_frequency_domain(self):
        return SignalFrameArray([frame.to_frequency_domain() for frame in self.items if frame.domain == "time"])


class TimeFrequencyFrameList(SignalCollection):
    # transform according to a function

    def __init__(self, items: List[TimeFrequencyFrame]):
        super().__init__(items)

    def select_range(self, start: float, end: float) -> List[TimeFrequencyFrame]:
        return [f for f in self.items if start <= f.start_time <= end]

    def group_slice_time(self, start, end):
        return TimeFrequencyFrameList([item.slice_time(start, end) for item in self.items if item.domain == "frequency"])

    def group_slice_frequency(self, f_start, f_end):
        return TimeFrequencyFrameList([item.slice_frequency(f_start, f_end) for item in self.items if item.domain == "time"])


class EmitterGroup:
    # Bias dict comparison (in what way?)

    def __init__(self, emitters: Dict[str, Emitter]):
        self.emitters = emitters

    def get_emitter(self, _id):
        return self.emitters[_id]

    def get_emitters_by_platform_type(self, platform_type):
        return [self.emitters[id] for id in self.emitters if self.emitters[id].platform_type is platform_type]

    # Bias dict merge
    def merge_biases(self, new_biases: Optional[Dict[str, Any]]):
        all_biases = {}
        [all_biases.update(emitter.known_bias) for emitter in self.emitters]
        all_biases.update(new_biases)
        return all_biases

    # search description fields in emitters
    def search_description(self, query: str):
        return [emitter.id for emitter in self.emitters if emitter.description.re.matches(query)]

    # get list of id
    def list_ids(self):
        return [emitter.id for emitter in self.emitters]

    # get list of description
    def list_descriptions(self):
        return [emitter.description for emitter in self.emitters]


class EMFieldArray(SignalCollection):

    def __init__(self, items: List[T]):
        super().__init__(items)


class SignalEventList(SignalCollection):

    def __init__(self, items: List[SignalEvent]):
        super().__init__(items)


class SignalMessageList(SignalCollection):

    def __init__(self, items: List[SignalMessage]):
        super().__init__(items)
