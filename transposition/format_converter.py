# Transposition Layer: Making the Invisible 'Perceivable'
# Converts raw EM data into formats that can be sensed and interacted with...

# TEXT:
#       JSON
#       RAW?
#       CSV
#       TSV
# BINARY
#       raster formats:         jpeg, gif, tiff,
#       vector formats:         SVG, OL vector,
#       serialized formats:     pickle, HD5,
#       data formats:           NetCDF, xioarray, ndarray

# READING FORMATS
# [FormatReader(format_type, data)]: accept a format_type and read data.
#       processed = FormatReader(format_type.CSV, data)        # read CSV data into an array
#
# read from array: This is the default, core op + JSON
# read from file of type 'format': Reading is semantic for some formats, and not all data is needed.
# read from store, database, persist layer: read off MQ, db or other structured store (an S3 bucket)

# WRITING FORMATS
# [FormatWriter(format_type, format_spec)]: accept a format_type (input), a format spec (output) and write data.
#       other = FormatProcessor(format_type.OtHeR, processed)
#
# Synthetic vision of SAR or IR signals