### signal_semiotics_toolkit/core/time_frequency_frame.py

import numpy as np
from typing import Optional, Dict, Any

class TimeFrequencyFrame:
    """
    Represents a signal as a matrix across time and frequency dimensions.
    Each cell captures intensity, amplitude, or complex energy.
    """

    def __init__(self,
                 start_time: float,
                 duration: float,
                 freq_min: float,
                 freq_max: float,
                 tf_matrix: np.ndarray,
                 metadata: Optional[Dict[str, Any]] = None):
        self.start_time = start_time
        self.duration = duration
        self.freq_min = freq_min
        self.freq_max = freq_max
        self.tf_matrix = tf_matrix  # 2D array: time (rows) x frequency (cols)
        self.metadata = metadata or {}

    def get_time_axis(self) -> np.ndarray:
        return np.linspace(self.start_time, self.start_time + self.duration, self.tf_matrix.shape[0])

    def get_freq_axis(self) -> np.ndarray:
        return np.linspace(self.freq_min, self.freq_max, self.tf_matrix.shape[1])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "start_time": self.start_time,
            "duration": self.duration,
            "freq_min": self.freq_min,
            "freq_max": self.freq_max,
            "tf_matrix": self.tf_matrix.tolist(),
            "metadata": self.metadata
        }

    def plot(self, cmap: str = "viridis") -> None:
        import matplotlib.pyplot as plt
        plt.imshow(
            self.tf_matrix,
            extent=[self.freq_min, self.freq_max, self.start_time + self.duration, self.start_time],
            aspect='auto',
            cmap=cmap
        )
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Time (s)")
        plt.title("Time-Frequency Frame")
        plt.colorbar(label="Amplitude or Energy")
        plt.show()

    def slice_time(self, t_start: float, t_end: float) -> 'TimeFrequencyFrame':
        """Slice the frame between two times."""
        total_rows = self.tf_matrix.shape[0]
        time_axis = self.get_time_axis()
        idx_start = np.searchsorted(time_axis, t_start)
        idx_end = np.searchsorted(time_axis, t_end)
        sliced_matrix = self.tf_matrix[idx_start:idx_end, :]
        new_duration = t_end - t_start
        return TimeFrequencyFrame(
            start_time=t_start,
            duration=new_duration,
            freq_min=self.freq_min,
            freq_max=self.freq_max,
            tf_matrix=sliced_matrix,
            metadata=self.metadata
        )

    def slice_frequency(self, f_start: float, f_end: float) -> 'TimeFrequencyFrame':
        """Slice the frame between two frequencies."""
        total_cols = self.tf_matrix.shape[1]
        freq_axis = self.get_freq_axis()
        idx_start = np.searchsorted(freq_axis, f_start)
        idx_end = np.searchsorted(freq_axis, f_end)
        sliced_matrix = self.tf_matrix[:, idx_start:idx_end]
        new_freq_min = f_start
        new_freq_max = f_end
        return TimeFrequencyFrame(
            start_time=self.start_time,
            duration=self.duration,
            freq_min=new_freq_min,
            freq_max=new_freq_max,
            tf_matrix=sliced_matrix,
            metadata=self.metadata
        )

    def energy(self) -> float:
        """Calculate total energy across the frame."""
        return np.sum(np.abs(self.tf_matrix)**2)
