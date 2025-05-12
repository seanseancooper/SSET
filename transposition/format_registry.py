#  Copyright (c) 2025 Sean D. Cooper
#
#  This source code is licensed under the MIT license found in the LICENSE file in the root directory of this source tree.
#
# format_registry.py

from typing import Callable, Dict, Optional, Any
import numpy as np


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


# === Format Domains ===

def make_format_domain(entries: Dict[str, Dict[str, str]]) -> Dict[str, DataFormat]:
    return {
        name: DataFormat(
            name,
            entry["mime"],
            entry["ext"],
            basic_reader,
            basic_writer
        ) for name, entry in entries.items()
    }

raster_formats = make_format_domain({
    "jpeg": {"mime": "image/jpeg", "ext": ".jpg"},
    "tiff": {"mime": "image/tiff", "ext": ".tiff"},
})

vector_formats = make_format_domain({
    "svg": {"mime": "image/svg+xml", "ext": ".svg"},
    "ol_vector": {"mime": "application/json", "ext": ".geojson"},
})

audio_formats = make_format_domain({
    "mp3": {"mime": "audio/mpeg", "ext": ".mp3"},
    "wav": {"mime": "audio/wav", "ext": ".wav"},
})

scientific_formats = make_format_domain({
    "hd5": {"mime": "application/x-hdf5", "ext": ".h5"},
    "netcdf": {"mime": "application/x-netcdf", "ext": ".nc"},
})

textual_formats = make_format_domain({
    "csv": {"mime": "text/csv", "ext": ".csv"},
    "tsv": {"mime": "text/tab-separated-values", "ext": ".tsv"},
    "json": {"mime": "application/json", "ext": ".json"},
    "pickle": {"mime": "application/octet-stream", "ext": ".pkl"},
})

array_formats = make_format_domain({
    "ndarray": {"mime": "application/octet-stream", "ext": ".npy"},
    "xioarray": {"mime": "application/x-xio", "ext": ".xio"},
})


# Unified Registry
format_registry: Dict[str, Dict[str, DataFormat]] = {
    "raster": raster_formats,
    "vector": vector_formats,
    "audio": audio_formats,
    "scientific": scientific_formats,
    "textual": textual_formats,
    "array": array_formats,
}


def list_available_formats():
    for domain, formats in format_registry.items():
        print(f"\n[DOMAIN] {domain.upper()}")
        for name, fmt in formats.items():
            print(f" - {name} ({fmt.mime_type}) -> {fmt.extension}")
