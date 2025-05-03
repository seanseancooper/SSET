# bitstream_extractor.py: Layered decoding of known protocols.
# Demodulation: Taking an AM/FM/PSK signal and extracting the baseband data.

class BitStreamExtrator:
    """ Taking an AM/FM/PSK signal and extract the baseband signal. """

    def __init__(self, signal, proc_options={}):
        self.signal = signal
        self.proc_options = {}
        self.extracted = None

    def config(self):
        pass

    def get_signal_type(self):
        signal_type = None
        # what characteristics define the modulation type?
        return signal_type

    def extract_AM_signal(am_signal, options):
        processed = None
        option = options['option']  # potential options for processing
        # do something with am_signal.
        # return extracted AM baseband signal
        yield processed

    def extract_FM_signal(fm_signal, options):
        processed = None
        option = options['option']
        yield processed

    def extract_ASK_signal(ask_signal, options):  # Amplitude Shift Keying (ASK)
        # The common operating mode of Ethernet uses a 4-level amplitude modulation (2 bits per symbol) with 8 ns symbols.
        processed = None
        option = options['option']
        yield processed

    def extract_FSK_signal(fsk_signal, options):  # Frequency Shift Keying (FSK)
        processed = None
        option = options['option']
        yield processed

    def extract_PSK_signal(psk_signal, options):  # Phase Shift Keying (PSK)
        # The simplest form is Binary PSK, a.k.a. BPSK, two levels of phase.
        # The simplest form is Quadrature Phase Shift Keying (QPSK), two levels of phase.
        processed = None
        option = options['option']
        yield processed

    def extract_QAM_signal(psk_signal, options):  # combine ASK and PSK? Quadrature Amplitude Modulation (QAM)
        # 16 QAM
        # 32 QAM
        # 64 QAM
        # 256 QAM

        processed = None
        option = options['option']
        yield processed

    def process_signal(self, signal, type, proc_options):

        type = type or self.get_signal_type()
        extracted = None
        extract_options = proc_options['proc_options']

        if type:  # modulation types

            MODULATION_TYPES = {
                "AM" : extract_AM_signal,
                "FM" : extract_FM_signal,
                "ASK": extract_ASK_signal,
                "FSK": extract_ASK_signal,
                "PSK": extract_PSK_signal,
            }

            ext_method = MODULATION_TYPES[type]
            ext_signal = ext_method(signal, extract_options)

        return ext_signal



