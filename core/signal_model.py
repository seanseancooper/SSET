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

        self.phase = None
        self.magnitude = None
        self.window = None
        self.set_magnitude_phase()  # calculate on init

    def get_timestamp(self):
        return self.timestamp

    def get_duration(self):
        return self.duration

    def get_carrier_freq(self):
        return self.carrier_freq

    def get_bandwidth(self):
        return self.bandwidth

    def get_data(self):
        return self.data

    def set_data(self, data: np.ndarray):
        self.data = data
        self.set_magnitude_phase()  # recalculate for new data

    def get_domain(self):
        return self.domain

    def get_metadata(self):
        return self.metadata

    def set_metadata(self, metadata: Optional[Dict[str, Any]]):
        self.metadata = metadata

    def get_phase(self):
        _, p = self.set_magnitude_phase()
        return p

    def get_magnitude(self):
        m, _ = self.set_magnitude_phase()
        return m

    def set_magnitude_phase(self):
        data = self.data                # default
        if self.domain == "frequency":  # 'mixed' TBD
            data = np.fft.fft(self.data)
        return  np.abs(data), np.angle(data)

    def get_window(self):
        return self.window

    def set_window(self, window: np.hamming, size: 100):
        self.window = window(size)

    def to_frequency_domain(self):
        if self.domain == "frequency":
            return self
        spectrum = np.fft.fft(self.data)  # data is time-domain
        self.set_magnitude_phase()
        return SignalFrame(
            timestamp=self.timestamp,
            duration=self.duration,
            carrier_freq=self.carrier_freq,
            bandwidth=self.bandwidth,
            data=np.abs(spectrum),
            domain="frequency",
            metadata=self.metadata
        ), (self.magnitude, self.phase)

    def to_time_domain(self):
        if self.domain == "time":
            return self
        waveform = np.fft.ifft(self.data)  # data is frequency-domain
        self.set_magnitude_phase()
        return SignalFrame(
            timestamp=self.timestamp,
            duration=self.duration,
            carrier_freq=self.carrier_freq,
            bandwidth=self.bandwidth,
            data=np.real(waveform),
            domain="time",
            metadata=self.metadata
        ), (self.magnitude, self.phase)
