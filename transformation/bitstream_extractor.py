#  Copyright (c) 2025 Sean D. Cooper
#
#  This source code is licensed under the MIT license found in the LICENSE file in the root directory of this source tree.
#

# bitstream_extractor.py: Layered decoding of known protocols.
# Demodulation: Taking an AM/FM/PSK signal and extracting the baseband data.

class BitStreamExtrator:
    """ Taking an AM/FM/PSK signal and extract the baseband signal. """

    def __init__(self, signal, proc_options):
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
        #  WHERE IS AM USED?
        #
        # Amplitude modulation is used in a variety of applications. Even though it is not as widely used as it was in
        # previous years in its basic format it can nevertheless still be found.
        #
        #     Broadcast transmissions:   AM is still widely used for broadcasting on the long, medium and short
        #     wave bands. It is simple to demodulate and this means that radio receivers capable of demodulating
        #     amplitude modulation are cheap and simple to manufacture. Nevertheless many people are moving to
        #     high quality forms of transmission like frequency modulation, FM or digital transmissions.
        #     Air band radio:   VHF transmissions for many airborne applications still use AM. . It is used for
        #     ground to air radio communications as well as two way radio links for ground staff as well.
        #     Single sideband:   Amplitude modulation in the form of single sideband is still used for HF radio
        #     links. Using a lower bandwidth and providing more effective use of the transmitted power this form
        #     of modulation is still used for many point to point HF links.
        #     Quadrature amplitude modulation:   AM is widely used for the transmission of data in everything from
        #     short range wireless links such as Wi-Fi to cellular telecommunications and much more. Effectively
        #     it is formed by having two carriers 90° out of phase.
        #
        # These form some of the main uses of amplitude modulation. However in its basic form, this form of modulation
        # is being used less as a result of its inefficient use of both spectrum and power.

        # One of the aspects associated with amplitude modulation is the sidebands that are generated.
        # These govern the bandwidth of the signal and as such they are of great importance.
        #
        # It is found that if a carrier is modulated with a single tone, e.g. 1 kHz, then two sidebands will appear,
        # one either side of the main carrier spaced by 1 kHz away from it.
        #
        # Similarly if modulation with a variety of frequencies, e.g. speech or music is used, then the sidebands
        # will spread out either side of the carrier, extended out by an amount equal tot he top frequencies used.

# A measure known as the modulation index is also important. This details the level of modulation used and the maximum level to which modulation can be increased before the level of distortion increases and extensive interference is caused to other channels.
        #
        # The modulation index is generally given as a percentage and can be increased to 100% before unwanted products and interference are caused outside the normal or allocated bandwidth of the signal.

        # A measure known as the modulation index is also important. This details the level of modulation used and the maximum level to which modulation can be increased before the level of distortion increases and extensive interference is caused to other channels.
        #
        # The modulation index is generally given as a percentage and can be increased to 100% before unwanted products and interference are caused outside the normal or allocated bandwidth of the signal.

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
        ext_signal = None
        extract_options = proc_options['proc_options']

        if type:  # modulation types

            MODULATION_TYPES = {
                "AM" : self.extract_AM_signal,
                "FM" : self.extract_FM_signal,
                "ASK": self.extract_ASK_signal,
                "FSK": self.extract_ASK_signal,
                "PSK": self.extract_PSK_signal,
            }

            ext_method = MODULATION_TYPES[type]
            ext_signal = ext_method(signal, extract_options)

        return ext_signal



