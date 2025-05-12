#  Copyright (c) 2025 Sean D. Cooper
#
#  This source code is licensed under the MIT license found in the LICENSE file in the root directory of this source tree.
#

import numpy as np

class DataFormat:

    def __init__(self):
        self.format_reader = None  # a class that reads the format
        self.format_reader_method = None  # method that reads
        self.format_reader_opts = None  # options passed to the reader.

        self.format_writer = None  # a class that writes the format
        self.format_writer_method = None  # method that writes
        self.format_writer_opts = None  # options passed to the writer.

        self.config = {}

    def read(self, file):
        read = f'{self.format_reader}.{self.format_reader_method}'
        array = np.ndarray  # read(file)
        return array

    def write(self, file, array):
        write = f'{self.format_writer}.{self.format_writer}'
        # return write(filename, array)

class FormatReader:

    def __init__(self, data_format: DataFormat, options):
        self.data_format = data_format
        self.data = None
        self.options = options or {}

    def read(self):
        self.data_format.read()

    def write(self, filename, array):
        self.data_format.write(filename, array)


# READING FORMATS
# raster formats: jpeg, tiff
class JpegFormatReader(FormatReader):
    pass

class TiffFormatReader(FormatReader):
    pass

class SVGFormatReader(FormatReader):
    pass

class OLVectorFormatReader(FormatReader):
    pass

class PickleFormatReader(FormatReader):
    pass

class HD5FormatReader(FormatReader):
    pass

class NetCDFFormatReader(FormatReader):
    pass

class NdArrayFormatReader(FormatReader):
    pass

class XioArrayFormatReader(FormatReader):
    pass

class JSONFormatReader(FormatReader):
    pass

class CSVFormatReader(FormatReader):
    pass

class TSVFormatReader(FormatReader):
    pass

class NetCDFFormatReader(FormatReader):
    pass

class MP3FormatReader(FormatReader):
    pass

class WAVFormatReader(FormatReader):
    pass

class FormatWriter:

    def __init__(self, data_format: DataFormat, options):
        self.data_format = data_format
        self.data = None
        self.options = options or {}

    def write(self, array):
        filename = ''
        self.data_format.write(filename, array)

# WRITING FORMATS
# [FormatWriter(format_type, format_spec)]: accept a format_type (input), a format spec (output) and write data.
#       other = FormatProcessor(format_type.OtHeR, processed)
#
# write to array: This is the default, core op + JSON.
# write to file of type 'format': this could be limited to a couple common raster formats (jpeg, tiff), but we
#       will also need 'vector' for maps & mapping. I don't believe it makes sense to write binary formats except HD5.
# write to store, database, persist layer: def write to MQ & Elastic for internal offline proccessing.


class FormatConverter:
    # Part of the Transposition layer: This class converts raw data into formats that can be interacted with.
    pass
