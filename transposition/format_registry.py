# format_registry.py

from typing import Callable, Dict, Optional, Any
import numpy as np
import pandas as pd
import json
import pickle
import csv
from PIL import Image
import h5py
import netCDF4
from scipy.io import wavfile
from pydub import AudioSegment


class DataFormat:
    def __init__(
        self,
        name: str,
        mime_type: str,
        extension: str,
        reader: Optional[Callable[..., np.ndarray]] = None,
        writer: Optional[Callable[..., Any]] = None,
        options: Optional[Dict[str, Any]] = None
    ):
        self.name = name
        self.mime_type = mime_type
        self.extension = extension
        self.reader = reader
        self.writer = writer
        self.options = options or {}

    def read(self, file_path: str) -> np.ndarray:
        if not self.reader:
            raise NotImplementedError(f"No reader implemented for {self.name}")
        return self.reader(file_path, **self.options)

    def write(self, file_path: str, array: np.ndarray):
        if not self.writer:
            raise NotImplementedError(f"No writer implemented for {self.name}")
        return self.writer(file_path, array, **self.options)


# Placeholder reader/writer implementations
def basic_reader(file_path: str, **kwargs):
    print(f"[READ] {file_path} with options {kwargs}")
    return np.zeros((10, 10))  # Dummy array


def basic_writer(file_path: str, array: np.ndarray, **kwargs):
    print(f"[WRITE] {file_path} with shape {array.shape} and options {kwargs}")
    return True


# Domain: Raster Formats
raster_formats = {
    "jpeg": DataFormat("jpeg", "image/jpeg", ".jpg", basic_reader, basic_writer),
    "tiff": DataFormat("tiff", "image/tiff", ".tiff", basic_reader, basic_writer),
}

# Domain: Vector / Mapping
vector_formats = {
    "svg": DataFormat("svg", "image/svg+xml", ".svg", basic_reader, basic_writer),
    "ol_vector": DataFormat("ol_vector", "application/json", ".geojson", basic_reader, basic_writer),
}

# Domain: Audio
audio_formats = {
    "mp3": DataFormat("mp3", "audio/mpeg", ".mp3", basic_reader, basic_writer),
    "wav": DataFormat("wav", "audio/wav", ".wav", basic_reader, basic_writer),
}

# Domain: Scientific
scientific_formats = {
    "hd5": DataFormat("hd5", "application/x-hdf5", ".h5", basic_reader, basic_writer),
    "netcdf": DataFormat("netcdf", "application/x-netcdf", ".nc", basic_reader, basic_writer),
}

# Domain: Tabular/Text
textual_formats = {
    "csv": DataFormat("csv", "text/csv", ".csv", basic_reader, basic_writer),
    "tsv": DataFormat("tsv", "text/tab-separated-values", ".tsv", basic_reader, basic_writer),
    "json": DataFormat("json", "application/json", ".json", basic_reader, basic_writer),
    "pickle": DataFormat("pickle", "application/octet-stream", ".pkl", basic_reader, basic_writer),
}

# Domain: Numpy
array_formats = {
    "ndarray": DataFormat("ndarray", "application/octet-stream", ".npy", basic_reader, basic_writer),
    "xioarray": DataFormat("xioarray", "application/x-xio", ".xio", basic_reader, basic_writer),
}


# === Format Registry (Plugin-Like Structure) ===
class FormatRegistry:
    def __init__(self):
        self.registry: Dict[str, DataFormat] = {}

    def register(self, name: str, format_obj: DataFormat):
        self.registry[name] = format_obj

    def get(self, name: str) -> Optional[DataFormat]:
        return self.registry.get(name)


def list_available_formats():
    for domain, formats in format_registry.items():
        print(f"\n[DOMAIN] {domain.upper()}")
        for name, fmt in formats.items():
            print(f" - {name} ({fmt.mime_type}) -> {fmt.extension}")


# Unified Registry
format_registry: Dict[str, Dict[str, DataFormat]] = {
    "raster": raster_formats,
    "vector": vector_formats,
    "audio": audio_formats,
    "scientific": scientific_formats,
    "textual": textual_formats,
    "array": array_formats,
}
