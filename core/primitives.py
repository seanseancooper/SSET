### signal_semiotics_toolkit/core/primitives.py

from typing import Optional, Dict, Any, Tuple, Union
import numpy as np


class Emitter:
    def __init__(self, id: str, description: str, platform_type: str, known_bias: Optional[Dict[str, Any]] = None):
        self.id = id
        self.description = description
        self.platform_type = platform_type
        self.known_bias = known_bias or {}

    def get_id(self):
        return self.id
    
    def get_description(self):
        return self.description

    def set_description(self, description:str):
        self.description = description
    
    def get_platform_type(self):
        return self.platform_type

    def set_platform_type(self, platform_type: str):
        self.platform_type = platform_type
    
    def get_known_bias(self):
        return self.known_bias

    def set_known_bias(self, known_bias: dict):
        self.known_bias = known_bias


class EMField:

    def __init__(
        self,
        timestamp: float,
        location: Tuple[float, float, Optional[float]],
        domain: str,
        data: np.ndarray,
        metadata: Optional[Dict[str, Any]] = None
    ):
        self.timestamp = timestamp
        self.location = location                # lat, lon, optional altitude. static or mutatable?
        self.domain = domain                    # 'time', 'frequency', 'spatial', 'symbolic'
        self.data = data
        self.metadata = metadata or {}

    def get_timestamp(self):
        return self.timestamp

    def get_location(self):
        return self.location

    def get_domain(self):
        return self.domain

    def get_data(self):
        return self.data

    def set_data(self, data: np.ndarray):
        self.data = data

    def get_metadata(self):
        return self.metadata

    def set_metadata(self, metadata: Optional[Dict[str, Any]]):
        self.metadata = metadata


class SignalEvent(EMField):
    def __init__(
        self,
        timestamp: float,
        location: Tuple[float, float, Optional[float]],
        domain: str,
        data: np.ndarray,
        duration: float,
        carrier_freq: float,
        bandwidth: float,
        emitter: Optional[Emitter] = None,
        modulation: Optional[str] = None,
        snr: Optional[float] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        super().__init__(timestamp, location, domain, data, metadata)
        self.duration = duration
        self.carrier_freq = carrier_freq
        self.bandwidth = bandwidth
        self.emitter = emitter
        self.modulation = modulation
        self.snr = snr

    def get_duration(self):
        return self.duration

    def get_carrier_freq(self):
        return self.carrier_freq

    def get_bandwidth(self):
        return self.bandwidth

    def get_emitter(self):
        return self.emitter

    def get_modulation(self):
        return self.modulation

    def get_snr(self):
        return self.snr


class SignalMessage(SignalEvent):
    def __init__(
        self,
        timestamp: float,
        location: Tuple[float, float, Optional[float]],
        domain: str,
        data: np.ndarray,
        duration: float,
        carrier_freq: float,
        bandwidth: float,
        decoded: Optional[Union[str, bytes, Dict]] = None,
        semantics: Optional[str] = None,
        emitter: Optional[Emitter] = None,
        modulation: Optional[str] = None,
        snr: Optional[float] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        super().__init__(timestamp, location, domain, data, duration, carrier_freq, bandwidth, emitter, modulation, snr, metadata)
        self.decoded = decoded
        self.semantics = semantics

    def get_decoded(self):
        return self.decoded

    def set_decoded(self, decoded: Optional[Union[str, bytes, Dict]]):
        self.decoded = decoded

    def get_semantics(self):
        return self.semantics

    def set_semantics(self, semantics: Optional[str]):
        self.semantics = semantics
