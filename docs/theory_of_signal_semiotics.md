### signal_semiotics_toolkit/README.md

# Signal Semiotics Toolkit

## Overview

This toolkit explores a foundational approach to interpreting electromagnetic (EM) emissions as a form of language.
We frame signal analysis through two core concepts: **transposition** (making signals perceptible) and
**transformation** (making signals intelligible).

By treating EM emissions as communicative acts rather than just data or interference, we gain affordances in analysis,
understanding, and potentially interaction. This approach draws from semiotics, signal processing, cognitive electronic
warfare, and information theory.

---

## Key Concepts

### Transposition
Convert EM emissions into a perceptible form:
- Audio renderings
- Visualizations (spectrograms, spatial mappings)
- Synthetic sensory interfaces (future work)

### Transformation
Apply algorithms or models to extract meaning:
- Modulation classification
- Protocol/bitstream decoding
- Behavioral and temporal modeling

### Signal Semiotics
Interpret EM fields as meaningful symbols:
- What system is speaking?
- What behavior is occurring?
- What is the emitter's intent?

## Toward a Theory of Signal Semiotics

Traditionally, signal analysis emphasizes decoding and classification. But if we take a step back, we see that every signal is a communicative act—embedded in a system of meaning.

A theoretical signal can be decomposed into three layers:

1. **Bias**: The structured, persistent signature or fingerprint of the emitter. This includes its choice of frequency, modulation, timing, and behavior. Bias encodes *intent*, *identity*, and *design constraints*. It is the emitter's grammar or dialect.

2. **Variance**: These are the modulations and variations around the bias that convey specific instances of content or behavior. This is where meaning fluctuates and where one can observe the "speech" or message, framed within the emitter's grammar.

3. **Noise**: Traditionally viewed as meaningless, noise can still carry semantic weight—especially when analyzed ecologically. Noise may reflect interference, jamming, multipath effects, or even deception. In a semiotic context, noise may be unintentional expression, or ambient context.

This mirrors linguistic and semiotic theory:
- **Bias** ≈ Syntax / Language Rules
- **Variance** ≈ Message / Utterance
- **Noise** ≈ Paralinguistic or Environmental Expression

When we acknowledge EM emissions as language-like, we gain new methods of interpreting them:
- Not just what a signal says, but **how** it says it.
- Not just whether a signal is present, but **why** it behaves that way.
- Not just identifying modulation, but **inferring motive or state**.

This model builds a foundation for tools that don't just classify signals—they *interpret* them.


---
--- 
# PREAMBLE
We experience the world in 3 dimensions, bounded and directed by time.
- Only forward moovement, hindsight.
- Missed dimensions, features, wrong ranges, imperceptible, unknown, functional or statistic.

What if we could mask or altogether remove these constraints through visualization, allowing us to see the unseen and know thee unknown?
# I. Transposition & Transformation.
- **Transposition**: Moving from A->B ... think "A *"
   - time-domain function: 'manipulation of A', 'A x many times'm 'timing' and 'timestamp'
   - related too frequency domain wrt a having been the label A for some observablee amount of time before being labeled B.
- **Transformation**: Changing A->B .... think "ƒ(A)"
   - frequency domain: function of acting on A, the result of processing A, Analysis of A
   - related to time domain wrt "being". Because ƒ exists and acts, it presumably "occurs" and produces "B", the result of the occurance of ƒ.

> Transposition and Transformation are interrelated.

This paradigm could be represented by the 'SignalFrame' type.
- Same fields for both time and frequency domains.
```python


    def to_frequency_domain(self):
        if self.domain == "frequency":
            return self
        spectrum = np.fft.fft(self.data)
        return SignalFrame(
            timestamp=self.timestamp,
            duration=self.duration,
            carrier_freq=self.carrier_freq,
            bandwidth=self.bandwidth,
            data=np.abs(spectrum),
            domain="frequency",
            metadata=self.metadata
        )

    def to_time_domain(self):
        if self.domain == "time":
            return self
        waveform = np.fft.ifft(self.data)
        return SignalFrame(
            timestamp=self.timestamp,
            duration=self.duration,
            carrier_freq=self.carrier_freq,
            bandwidth=self.bandwidth,
            data=np.real(waveform),
            domain="time",
            metadata=self.metadata
        )


```
- Encapsulates features across a variety of spectra (EM Field)
- Contains structures to encapsulate a variety of 'symbols' representing semiotic information contained /derived from signal 'features' (communications theory)

### 📐 Metadata as an Extensible Symbol Layer

The metadata dict is where semiotic affordances can begin:
```json
    
    

        {
          "emitter_id": "DEMOD_X3",
          "modulation": "QPSK",
          "intent": "Beacon",
          "environment": "Urban, Multi-path",
          "confidence": 0.87
        }

```
We can even embed context over time:
```json


        "history": [
          {"t": 0, "modulation": "CW"},
          {"t": 5, "modulation": "QPSK"},
          {"t": 10, "modulation": "Noise Burst"}
        ]
     ]

```
> #### SignalFrames occur at a "_sampling rate_".

# II. "It's All EM Field"

Humans can perceive a wide range of sounds, typically from 20 Hz to 20,000 Hz, and light wavelengths between 380 and 750 nanometers. This translates to an audible spectrum encompassing a wide range of pitches and a visual spectrum encompassing the colors we see. -- https://www.google.com/search?q=rannge+of+humabn+perception+vvission%2C+hearing&oq=rannge+of+humabn+perception+vvission%2C+hearing&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTE5MTkxajBqN6gCALACAA&sourceid=chrome&ie=UTF-8

"A radio wave is a form of light. This is an unusual thought for many people so we must again revisit the concept of the entire Electromagnetic Spectrum. In the entire spectrum, visible light is only a very small portion of the Electromagnetic Spectrum. X-Rays, for example, are also light but you cannot see them. The same can be said for Infrared light, which can only be detected using special equipment. So a radio wave is just another wave of light that cannot be seen by human eyes. But, they are all around us and they have many common properties with visible light. Radio waves travel at the same speed as light � approximately 186,000 miles per second." -- https://www.universalclass.com/articles/self-help/ham-radio-basics.htm

![EM_Spectrum_Properties_edit.svg.jpg](images/EM_Spectrum_Properties_edit.svg.jpg)

Transposition: Movving from A to B

- Changes fro one frequency/frequeny range to another
- Informatioon ccannot exist before it exists. (feature=change)
- implies cchange in 'rate'
- Manipulatioon of sampling rate is the tool.
>- we ccannnot change the event only observe it.
>- the only logical thing to innstrument is the SR, we ccan't change anything else.


#### investigate...
- compression/expansion effects during transpoosition (time domain scaling/freq domain invversee scaling)
- error rate during transpoositionn (pure math vvs. reality)
>- optimization  problem.
- changes in 'dynamics' in transposition and inter-relational changes in feature dynamics in transposition.
- Q: did it occur instantaineously?: Nope. Took some time no matter hoow small -> "speed of reality"

# III. Semiotic Relationship Between 'Signal' and Meaning

![semiotic.jpg](images/semiotic.jpg)
> Communications theory assigns three roles:
> - '**symbol**': The _signal_. That which 'contains' information, and is composed of 'bias', 'variance', and 'noise'.
> - '**actor**': The _recipient_. That which acts/understands on information contained in the signal.
> - '**meaning**': The _understanding_. That which endows a symbol as/with information to the recipient.
> Because we can observe the actor, we could infer the meaning of the symbol.
> Having enough 'observations' and 'meanings', we can form a 'language' based on the symbols.

![signalframe.jpg](images/signalframe.jpg)

A SignalFrame type can be operationalized to allow Large Language Models to infer pattern and meaning via automated observation.

These observations can be serialized to form observations of the time/frequency domain features (signal) and arbitrary information (symbols) inherent in the signal manifestation. 


# IV. Tools for Signal Semiotics

Planning for development of SSET toolkit and API assets.
> ### A. Core Functionality 
>- Acessors/Mutators for fields
>- Collections API (deal with collections of SignalFrame type)
>  - operations on collections
>  - create/manipulate collections
>    - functional interfaces, programming
>- Processing the type
>  - SR manipulation
>  - FFT/IFFT
>    - core functionality, performance. speed needed here.
>  - time/freq domain manipulations
>    - deal with time, frequency features 'well'.
>  - Functional / User / Synthetic interfaces to manipulate data ad hoc.
> ### B. Visualization of Types and Collections of Types
>- reading data formats
>- transforming data formats
>- writing data formats
>- Interfaces, Integrations with Visualization Tools and Libraries.
>- - d3.js, MPL, Pandas, Seaborn, etc.
>  - Kibana, Graphana, dashboards
>  - Geospatial imaging tools
>- 