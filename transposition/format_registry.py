#  Copyright (c) 2025 Sean D. Cooper
#
#  This source code is licensed under the MIT license found in the LICENSE file in the root directory of this source tree.
#
# format_registry.py
from typing import Callable, Dict, Optional, Any
import numpy as np
import csv
from PIL import Image
from scipy.io import wavfile
import h5py
import netCDF4

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


# === Reader/Writer Implementations ===

def csv_reader(file_path: str, **kwargs) -> np.ndarray:
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = [list(map(float, row)) for row in reader]
    return np.array(data)

def csv_writer(file_path: str, array: np.ndarray, **kwargs):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in array:
            writer.writerow(row)
    return True

def jpeg_reader(file_path: str, **kwargs) -> np.ndarray:
    img = Image.open(file_path).convert("RGB")
    return np.array(img)

def jpeg_writer(file_path: str, array: np.ndarray, **kwargs):
    img = Image.fromarray(array.astype('uint8'))
    img.save(file_path, format='JPEG')
    return True

def wav_reader(file_path: str, **kwargs) -> np.ndarray:
    rate, data = wavfile.read(file_path)
    return data.astype(np.float32) / np.iinfo(data.dtype).max

def wav_writer(file_path: str, array: np.ndarray, **kwargs):
    rate = kwargs.get("rate", 44100)
    scaled = (array * 32767).astype(np.int16)
    wavfile.write(file_path, rate, scaled)
    return True

def netcdf_reader(file_path: str, **kwargs) -> np.ndarray:
    with netCDF4.Dataset(file_path, 'r') as ds:
        var_name = kwargs.get("variable") or list(ds.variables.keys())[0]
        return ds.variables[var_name][:]

def netcdf_writer(file_path: str, array: np.ndarray, **kwargs):
    with netCDF4.Dataset(file_path, 'w', format='NETCDF4') as ds:
        ds.createDimension('dim0', array.shape[0])
        if array.ndim > 1:
            ds.createDimension('dim1', array.shape[1])
        dims = ('dim0',) if array.ndim == 1 else ('dim0', 'dim1')
        var = ds.createVariable('data', 'f4', dims)
        var[:] = array
    return True

def xioarray_reader(file_path: str, **kwargs) -> np.ndarray:
    return np.load(file_path)

def xioarray_writer(file_path: str, array: np.ndarray, **kwargs):
    np.save(file_path, array)
    return True

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

# Replace basic reader/writer with real ones
textual_formats["csv"].reader = csv_reader
textual_formats["csv"].writer = csv_writer

raster_formats["jpeg"].reader = jpeg_reader
raster_formats["jpeg"].writer = jpeg_writer

audio_formats["wav"].reader = wav_reader
audio_formats["wav"].writer = wav_writer

scientific_formats["netcdf"].reader = netcdf_reader
scientific_formats["netcdf"].writer = netcdf_writer

array_formats["xioarray"].reader = xioarray_reader
array_formats["xioarray"].writer = xioarray_writer

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
