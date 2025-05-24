#  Copyright (c) 2025 Sean D. Cooper
#
#  This source code is licensed under the MIT license found in the LICENSE file in the root directory of this source tree.
#

from format_registry import DataFormat, format_registry, find_format

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


# this is wrong; there is no convert_to() method in the returned 'mapping' or its' objects.
def convert_format(source_path, target_path, source_format, target_format):
    find_format(source_format).convert_to(find_format(target_format), source_path, target_path)

