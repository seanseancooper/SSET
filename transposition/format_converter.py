#  Copyright (c) 2025 Sean D. Cooper
#
#  This source code is licensed under the MIT license found in the LICENSE file in the root directory of this source tree.
#

from typing import Callable, Dict, Optional, Type, Any
import pandas as pd
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
raster_formats = {
    "jpeg": DataFormat("jpeg", "image/jpeg", ".jpg", basic_reader, basic_writer),
    "tiff": DataFormat("tiff", "image/tiff", ".tiff", basic_reader, basic_writer),
}

class JpegFormatReader(FormatReader):
    pass


class TiffFormatReader(FormatReader):
    pass

# Domain: Vector / Mapping
vector_formats = {
    "svg": DataFormat("svg", "image/svg+xml", ".svg", basic_reader, basic_writer),
    "ol_vector": DataFormat("ol_vector", "application/json", ".geojson", basic_reader, basic_writer),
}


class SVGFormatReader(FormatReader):
    pass


class OLVectorFormatReader(FormatReader):
    pass

# Domain: Tabular/Text
textual_formats = {
    "csv": DataFormat("csv", "text/csv", ".csv", basic_reader, basic_writer),
    "tsv": DataFormat("tsv", "text/tab-separated-values", ".tsv", basic_reader, basic_writer),
    "json": DataFormat("json", "application/json", ".json", basic_reader, basic_writer),
    "pickle": DataFormat("pickle", "application/octet-stream", ".pkl", basic_reader, basic_writer),
}


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
scientific_formats = {
    "hd5": DataFormat("hd5", "application/x-hdf5", ".h5", basic_reader, basic_writer),
    "netcdf": DataFormat("netcdf", "application/x-netcdf", ".nc", basic_reader, basic_writer),
}

class HD5FormatReader(FormatReader):
    pass

class NetCDFFormatReader(FormatReader):
    pass


# Domain: Numpy
array_formats = {
    "ndarray": DataFormat("ndarray", "application/octet-stream", ".npy", basic_reader, basic_writer),
    "xioarray": DataFormat("xioarray", "application/x-xio", ".xio", basic_reader, basic_writer),
}


class NdArrayFormatReader(FormatReader):
    pass


class XioArrayFormatReader(FormatReader):
    pass



# Domain: Audio
audio_formats = {
    "mp3": DataFormat("mp3", "audio/mpeg", ".mp3", basic_reader, basic_writer),
    "wav": DataFormat("wav", "audio/wav", ".wav", basic_reader, basic_writer),
}


class MP3FormatReader(FormatReader):
    pass


class WAVFormatReader(FormatReader):
    pass


# === Converter ===

class FormatConverter:
    def __init__(self, source_format: DataFormat, target_format: DataFormat):
        self.source_format = source_format
        self.target_format = target_format

    def convert(self, read_opts: Dict[str, Any] = {}, write_opts: Dict[str, Any] = {}):
        reader = self.source_format.get_reader(**read_opts)
        data = reader.read()

        writer = self.target_format.get_writer(**write_opts)
        writer.write(data)

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
