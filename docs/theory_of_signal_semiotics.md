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
# 0. PREAMBLE
We experience the world in 3 dimensions, bounded and directed by time. It is both 'unidirectional' AND a sequencing mechanism.
- Only forward moovement, hindsight.
- Missed dimensions, features, wrong ranges, imperceptible, unknown, functional or statistic.

Visualization is a perceptual prosthesis for understanding 'hidden' dimensions; We often miss features that are hidden across imperceptible dimensions—be they statistical, functional, or entirely unknown. 

What if we could mask or altogether remove these constraints through visualization, allowing us to 'see the unseen' and 'know the unknown'? 


# 1. Transposition & Transformation.
- ### **Transposition**: Moving from A -> B 
   - think "A *", many consecutive "A" moving to "B".
   - time-domain function: 'manipulation of A', 'A x many times', 'timing' or 'timestamp'..
   - implies a collection of 'time-shifted' A.
   - related to frequency domain wrt. a having been the label A for some observable amount of time before being labeled B; a 're-labelling' operation that _may_ be sample rate driven.
- ### **Transformation**: Changing A->B
   - think "ƒ(A)"
   - transformation can also occur in time (e.g., modulation)
   - Frequency domain function: function of acting on A, the result of processing A, Analysis of A
   - Related to time domain wrt "being". Because ƒ exists and acts, it presumably "occurs" and produces "B", the result of the occurrence of ƒ. "ƒ is a functional operator acting on A, producing B as an analyzable outcome."

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

The metadata dict is where semiotic affordances can begin. Metadata fields are interpretable hooks, not guarantees of truth. Especially in using ML inference:
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

History could be structured as a field inside metadata):
```json
"metadata": {
  ...
  "history": [
    {"t": 0, "modulation": "CW"},
    {"t": 5, "modulation": "QPSK"}
  ]
}

```

> #### SignalFrames occur at a "_sampling rate_".

# 2. "It's All EM Field"

Laying the groundwork for a unified sensory mapping, applying transposition as a meta-concept that refers to any shift across representational domains (e.g., time to frequency), including frequency shifts, whether en masse or discrete.

In music, "transposition" means shifting a signal up or down in pitch — which is a frequency shift. You're invoking that metaphor in a way that extends beyond music, and it fits well with how frequency hopping, spectral analysis, and retargeting across domains works.

Distinction from Modulation matters; Modulation does often include changes in frequency (e.g., FM), but what distinguishes modulation is the encoding of information through variation — of amplitude, phase, frequency, or another carrier property. Modulation can be a mechanism of transposition, but not all transpositions are modulations.



"Humans can perceive a wide range of sounds, typically from 20 Hz to 20,000 Hz, and light wavelengths between 380 and 750 nanometers. This translates to an audible spectrum encompassing a wide range of pitches and a visual spectrum encompassing the colors we see. -- https://www.google.com/search?q=rannge+of+humabn+perception+vvission%2C+hearing&oq=rannge+of+humabn+perception+vvission%2C+hearing&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTE5MTkxajBqN6gCALACAA&sourceid=chrome&ie=UTF-8

"A radio wave is a form of light. This is an unusual thought for many people so we must again revisit the concept of the entire Electromagnetic Spectrum. In the entire spectrum, visible light is only a very small portion of the Electromagnetic Spectrum. X-Rays, for example, are also light but you cannot see them. The same can be said for Infrared light, which can only be detected using special equipment. So a radio wave is just another wave of light that cannot be seen by human eyes. But, they are all around us and they have many common properties with visible light. Radio waves travel at the same speed as light � approximately 186,000 miles per second." -- https://www.universalclass.com/articles/self-help/ham-radio-basics.htm

![EM_Spectrum_Properties_edit.svg.jpg](images/EM_Spectrum_Properties_edit.svg.jpg)

Transposition: Moving from A to B

- Changes fro one frequency/frequeny range to another
- Informatioon ccannot exist before it exists. (feature=change)
- implies change in 'rate'
- Manipulatioon of sampling rate is the tool.
>- We cannot alter the originating event, but we can alter how we sample and represent it.
>- the only logical thing to instrument is sample rate, we can't change anything else.


#### investigate...
- compression/expansion effects during transposition (time domain scaling/freq domain inverse scaling)
- error rate during transposition: Explore how ideal mathematical transformations diverge from physical or noisy implementations.
>- optimization  problem.
- changes in 'dynamics' in transposition and inter-relational changes in feature dynamics in transposition.
- Q: did it occur instantaneously?: Nope. Took some time no matter how small -> "the speed of reality"

# 3. Semiotic Relationship Between 'Signal' and Meaning

![semiotic.jpg](images/semiotic.jpg)
> Communications theory assigns three roles:
> - '**symbol**': The _signal_. That which 'contains' information.. Symbols are structured patterns within the signal, influenced by and composed of 'bias', 'variance', and 'noise'.
> - '**actor**': The _recipient_. That which acts/understands on information contained in the signal.
> - '**meaning**': The _understanding_. That which endows a symbol as/with information to the recipient.
>   - Because we can observe the actor, we could infer the meaning of the symbol. In this case, referring to semiotic inference via system output: if an automated agent receives a signal and then takes action, we can treat that action as the output of its interpretation. This lets us reverse-engineer meaning.
>   - Having enough 'observations' and 'meanings', we can form a 'language' based on the symbols.
>> That’s fundamentally how machine learning models learn meaning through interaction.

>> “By observing the behavior of the actor in response to a symbol, we can infer the meaning that the actor has ascribed to it — allowing us to construct a language of signal interpretation through automated observation.”

```commandline
[Signal (Symbol)] → [Actor System] → [Response] → [Observer System] → [Inferred Meaning]

```

![signalframe.jpg](images/signalframe.jpg)

A SignalFrame type can be operationalized to allow Large Language Models to infer pattern and meaning via automated observation.

These observations can be serialized to form observations of the time/frequency domain features (signal) and arbitrary information (symbols) inherent in the signal manifestation. 

# 4. Tools for Signal Semiotics

Planning for development of SSET toolkit and API assets.
> ### A. Core Functionality & Collections
>- Accessors/Mutators for fields
>- Collections API (deal with collections of SignalFrame type)
>  - operations on collections
>  - create/manipulate collections
>    - functional interfaces, programming
>- Processing the SignalFrame type
>  - SR manipulation
>  - FFT/IFFT
>    - core functionality, performance. speed needed here.
>  - time/freq domain manipulations
>    - sequencing and timeline analysis.
>    - deal with time, frequency features 'well'.
>  - Functional / User / Synthetic interfaces to manipulate data ad hoc.
> ### B. Visualization of Types
>- displaying data contained within the type. 
>- reading data formats
>- transforming data formats
>- writing data formats
>- Interfaces, Integrations with 3rd party visualization tools and libraries.
>- - d3.js, MPL, Pandas, Seaborn, etc.
>  - Kibana, Graphana, dashboards
>  - Geospatial imaging tools
> ### C. Inference
>- Integrates LLMs or ML classifiers.
>  - pattern discover. 
>  - Inference, prediction and semantic/semiotic extraction 
>  - semiotic classification .

> 