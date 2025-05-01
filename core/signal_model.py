import numpy as np
from typing import Optional, Dict, Any


class SignalFrame:
    def __init__(
        self,
        timestamp: float,
        duration: float,
        carrier_freq: float,
        bandwidth: float,
        data: np.ndarray,
        domain: str = "time",
        metadata: Optional[Dict[str, Any]] = None
    ):
        """
        Represents a segment or 'frame' of an EM signal in either time or frequency domain.

        Parameters:
        - timestamp: Time of capture (seconds since epoch)
        - duration: Duration of the frame in seconds
        - carrier_freq: Central frequency in Hz
        - bandwidth: Signal width in Hz
        - data: Array representing IQ samples, power spectrum, or waveform
        - domain: 'time', 'frequency', or future: 'mixed'
        - metadata: Arbitrary static or dynamic metadata
        """

        self.timestamp = timestamp
        self.duration = duration
        self.carrier_freq = carrier_freq
        self.bandwidth = bandwidth
        self.data = data
        self.domain = domain
        self.metadata = metadata or {}

    # 📐 Metadata as an Extensible Symbol Layer
    # The metadata dict is where semiotic affordances can begin:
    #
    #     {
    #       "emitter_id": "DEMOD_X3",
    #       "modulation": "QPSK",
    #       "intent": "Beacon",
    #       "environment": "Urban, Multi-path",
    #       "confidence": 0.87
    #     }
    #
    #
    # We can even embed context over time:
    #
    #     "history": [
    #       {"t": 0, "modulation": "CW"},
    #       {"t": 5, "modulation": "QPSK"},
    #       {"t": 10, "modulation": "Noise Burst"}
    #     ]

    def to_frequency_domain(self):
        if self.domain == "frequency":
            return self
        spectrum = np.fft.fft(self.data)
        return SignalFrame(
            timestamp=self.timestamp,
            duration=self.duration,
            carrier_freq=self.carrier_freq,
            bandwidth=self.bandwidth,
            data=np.abs(spectrum),
            domain="frequency",
            metadata=self.metadata
        )

    def to_time_domain(self):
        if self.domain == "time":
            return self
        waveform = np.fft.ifft(self.data)
        return SignalFrame(
            timestamp=self.timestamp,
            duration=self.duration,
            carrier_freq=self.carrier_freq,
            bandwidth=self.bandwidth,
            data=np.real(waveform),
            domain="time",
            metadata=self.metadata
        )
