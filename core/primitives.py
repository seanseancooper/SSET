### signal_semiotics_toolkit/core/primitives.py

from typing import Optional, Dict, Any, Tuple, Union
import numpy as np

class Emitter:
    def __init__(self, id: str, description: str, platform_type: str, known_bias: Optional[Dict[str, Any]] = None):
        self.id = id
        self.description = description
        self.platform_type = platform_type
        self.known_bias = known_bias or {}

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


        # is this location field static or mutated after the fact?
        # What about signals having sources vs. being received?
        # is this indicative of a position (where I am in the scope of
        # the EMField) or a location (where the EMField is emanating from)
        self.location = location  # lat, lon, optional altitude
        self.domain = domain  # 'time', 'frequency', 'spatial', 'symbolic'
        self.data = data
        self.metadata = metadata or {}

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

