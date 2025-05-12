#  Copyright (c) 2025 Sean D. Cooper
#
#  This source code is licensed under the MIT license found in the LICENSE file in the root directory of this source tree.
#

from format_registry import DataFormat, format_registry

from typing import Callable, Dict, Optional, Any
import pandas as pd

# For raster images
from PIL import Image           # JPEG, TIFF, PNG

# For scientific data formats
import h5py                     # HDF5
import netCDF4                  # NetCDF

# For audio formats
from scipy.io import wavfile    # WAV
from pydub import AudioSegment  # MP3, WAV

# For vector and geo formats
import json
import geopandas as gpd         # GeoJSON / OL vector

# For tabular data
import csv                      # CSV/TSV
import pickle                   # Pickle

# For NumPy binary
import numpy as np              # NPY


# Placeholder reader/writer implementations
def basic_reader(file_path: str, **kwargs):
    print(f"[READ] {file_path} with options {kwargs}")
    return np.zeros((10, 10))  # Dummy array


def basic_writer(file_path: str, array: np.ndarray, **kwargs):
    print(f"[WRITE] {file_path} with shape {array.shape} and options {kwargs}")
    return True


class FormatReader:
    def __init__(self, data_format: DataFormat, options: Optional[Dict[str, Any]] = None):
        self.data_format = data_format
        self.options = options or {}

    def read(self):
        raise NotImplementedError


class FormatWriter:
    def __init__(self, data_format: DataFormat, options: Optional[Dict[str, Any]] = None):
        self.data_format = data_format
        self.options = options or {}

    def write(self, array):
        raise NotImplementedError


# Domain: Raster Formats
class JpegFormatReader(FormatReader):
    pass


class TiffFormatReader(FormatReader):
    pass


# Domain: Vector / Mapping
class SVGFormatReader(FormatReader):
    pass


class OLVectorFormatReader(FormatReader):
    pass


# Domain: Tabular/Text
class CSVFormatReader(FormatReader):
    def read(self):
        path = self.options.get("path")
        return pd.read_csv(path)


class CSVFormatWriter(FormatWriter):
    def write(self, array):
        path = self.options.get("path")
        pd.DataFrame(array).to_csv(path, index=False)


class TSVFormatReader(FormatReader):
    pass


class JSONFormatReader(FormatReader):
    pass


class JSONFormatWriter(FormatWriter):
    def write(self, array):
        path = self.options.get("path")
        pd.DataFrame(array).to_json(path)


class PickleFormatReader(FormatReader):
    pass


# Domain: Scientific
class HD5FormatReader(FormatReader):
    pass


class NetCDFFormatReader(FormatReader):
    pass


# Domain: Numpy
class NdArrayFormatReader(FormatReader):
    pass


class XioArrayFormatReader(FormatReader):
    pass


# Domain: Audio
class MP3FormatReader(FormatReader):
    pass


class WAVFormatReader(FormatReader):
    pass


def find_format(name: str) -> DataFormat:
    for domain_formats in format_registry.values():
        if name in domain_formats:
            return domain_formats[name]
    raise ValueError(f"Format '{name}' not found in registry")


def convert_format(source_path: str, target_path: str, source_format: str, target_format: str):
    source_fmt = find_format(source_format)
    target_fmt = find_format(target_format)

    data = source_fmt.read(source_path)
    target_fmt.write(target_path, data)


# === Converter ===
class FormatConverter:
    """ Implements logic to convert between formats using registered reader/writer pairs. """
    def __init__(self, source_format: DataFormat, target_format: DataFormat):
        self.source_format = source_format
        self.target_format = target_format


