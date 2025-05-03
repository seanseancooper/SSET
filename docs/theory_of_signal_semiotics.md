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
- ### **Transformation**: Changing A -> B
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

> frequencies down to DC (0 Hz). We can’t transmit DC.

```
+----------------------------+--------+---------+---------+---------+----------+------------+
|                            | HUMAN  | FELIDAE | CANIDAE |  AVES   | INSECTA  | OLFACTORES |
+----------------------------+--------+---------+---------+---------+----------+------------+
| Speed of Perception (Hz)   | 60     | 70      | 75      | 100     | 300      | 80         |
| Bandwidth of Vision (Hz)   | 400–790| 400–740 | 400–750 | 300–700 | 300–650  | 400–750    |
| Bandwidth of Hearing (Hz)  | 20–20k | 48–85k  | 40–60k  | 1–4k    | 100–10k  | 20–20k     |
| Field of View (degrees)    | 210    | 200     | 250     | 300     | 360      | 220        |
| Resolution (Words/Minute)  | 250    | 100     | 120     | 150     | 200      | 130        |
| Quantity of Symbols        | 50k    | 100     | 150     | 200     | 300      | 500        |
| Longest Word               | 45     | 10      | 12      | 15      | 20       | 25         |
| Shortest Word              | 1      | 1       | 1       | 1       | 1        | 1          |
| Most Frequent Word         | 'the'  | 'meow'  | 'bark'  | 'chirp' | 'buzz'   | 'grunt'    |
+----------------------------+--------+---------+---------+---------+----------+------------+

SYMBOL: Perception of Symbols.
| Speed of Perception (Hz)   
| Bandwidth of Vision (Hz)   
| Bandwidth of Hearing (Hz)
| Field of View (degrees)    
| Resolution (Words/Minute)  

MEANING: Size and Distibution of Symbols in Linguistic Context
| Quantity of Symbols        
| Longest Word               
| Shortest Word              
| Most Frequent Word    

ACTOR: Semantics, Interpretations, Synonyms for Symbols
+----------------------------
```

---

# Chapter 6: Language Compression and the Biological Foundations of Symbolic Systems

## Overview

This chapter explores how perceptual constraints in biological organisms shape their language systems, focusing on the capacity to distinguish and use symbols. We examine the relationship between sensory bandwidth, symbol resolution, ecological context, and language structure across different classes of organisms. We also explore the potential for formalizing a mathematical model of language that accounts for these constraints and the implications for artificial systems.

## 1. Symbols vs. Words

* **Symbol**: A discrete perceptual unit that carries meaning; may or may not be contextually complete. Example: "eggplant" (a symbol that could be a visual, olfactory, or auditory pattern).
* **Word**: A structured collection of symbols intended to form a complete unit of meaning within a context. Words are typically used to establish connections between ideas or agents.

In this framework, symbols are the atomic units, while words are composite structures used for higher-order contextual communication.

## 2. Perceptual Constraints and Symbol Resolution

Organisms differ in their ability to perceive and resolve symbols due to variations in:

* **Speed of Perception (Hz)**: How quickly symbols can be perceived as discrete units.
* **Bandwidth of Vision and Hearing**: The frequency range over which symbols can be received.
* **Field of View**: The spatial range of visual symbols.
* **Resolution (WPM)**: The rate at which symbols can be processed or interpreted.

These factors define the size of the perceivable symbol set and therefore constrain the linguistic expressiveness of a species.

## 3. Species Comparison Table

A structured table was developed to compare perception-based symbol use across species (Humans, Felidae, Canidae, Aves, Insecta, Olfactores, and Machina). Metrics included perceptual speed, sensory bandwidth, visual field, symbolic resolution, and linguistic structure.

The key insight: **species adapt their symbolic systems to fit within the constraints of their sensory modalities and ecological context**. Birds, for example, may use rapid symbol perception to enable complex calls, even with a narrower auditory bandwidth. Insects may rely more heavily on chemical signals due to low visual or auditory bandwidth.

## 4. Language Compression as an Evolutionary Strategy

Language compression arises naturally under the constraint of limited perception. Systems must economize:

* **Symbol use**: fewer, multi-functional symbols
* **Repetition**: frequent reuse of core symbols
* **Contextual layering**: multiple meanings encoded into symbol variation (tone, repetition, pattern)

This is not a limitation—it is a strategic compression. Symbolic efficiency maximizes transmission under real-world biological constraints.

## 5. Toward a Semiotic Language Model

We posit a functional model:

```math
L = f(S, B, R, C)
```

Where:

* `L`: Communicative language capacity
* `S`: Symbolic resolution (rate of symbol perception)
* `B`: Bandwidth of perception (range of signal frequency)
* `R`: Repertoire size (distinct symbols that can be retained)
* `C`: Cognitive-contextual range (mental states that can be symbolically represented)

Examples:

* **Humans**: Moderate `S`, High `B`, High `R`, High `C`
* **Birds**: High `S`, Moderate `B`, Low `R`, Moderate `C`
* **Insects**: Moderate `S`, Low `B`, Low `R`, Low `C`
* **AI**: Potentially High `S`, High `B`, Infinite `R`, Simulated `C`

This model can be used to predict or constrain the form and limits of symbolic systems across domains.

## 6. Implications for Signal Semiotics

Understanding the biological foundations of perception and symbolic resolution helps us:

* Design communication systems that are compatible with sensory constraints (e.g. robots, assistive tech)
* Interpret non-human communication systems in ecological and cognitive terms
* Build synthetic languages or translation systems that compress or expand symbols intelligently

The broader implication is that **meaning and language are not abstract universals, but grounded in perceptual embodiment and ecological necessity**.

This understanding is core to advancing the Signal Semiotics framework into a predictive, designable system of symbolic representation across diverse agents, biological or synthetic.


---

Here is a refined and cross-validated ASCII text table that retains and organizes the previously discussed data across species and categories, integrating perceptual limits and inferred symbolic capacity. It aligns with the structured chapter and reflects the distinction between *symbols* and *words*, as clarified.

---

### 🧠 Semiotic Table: Species Perceptual and Symbolic Language Properties

#### SYMBOL Category – Perception of Symbols

| Metric                    | HUMAN         | Felidae       | Canidae       | Aves          | Insecta      | Olfactores    | Machina   |
| ------------------------- | ------------- | ------------- | ------------- | ------------- | ------------ | ------------- | --------- |
| Speed of Perception (Hz)  | \~60 Hz       | \~55 Hz       | \~40 Hz       | \~120 Hz      | \~250 Hz     | \~30–60 Hz    | 1–10⁶ Hz  |
| Vision Bandwidth (Hz)     | \~430–770 THz | \~400–700 THz | \~400–700 THz | \~300–800 THz | minimal      | \~400–700 THz | Full spec |
| Hearing Bandwidth (Hz)    | 20–20k Hz     | 55–77k Hz     | 40–60k Hz     | 1–4k Hz       | Vib: 10–1kHz | 40–20k Hz     | 1–1M+ Hz  |
| Field of View (°)         | \~210°        | \~200°        | \~250°        | \~300°        | \~360°       | \~270°        | 360° sim. |
| Symbol Discern Rate (WPM) | \~250 WPM     | \~50 est.     | \~70 est.     | \~500 est.    | \~900 est.   | \~40 est.     | >10⁶ est. |

---

#### MEANING Category – Symbolic Context, Compression, Distribution

| Metric                    | HUMAN        | Felidae        | Canidae        | Aves          | Insecta     | Olfactores     | Machina       |
| ------------------------- | ------------ | -------------- | -------------- | ------------- | ----------- | -------------- | ------------- |
| Distinct Symbol Types     | \~50k (lex.) | \~100–300 est. | \~300–500 est. | \~500–1k est. | \~200 est.  | \~200–400 est. | \~∞ (struct.) |
| Avg. Symbol String Length | \~5–15       | 1–2 est.       | 1–3 est.       | 2–4 est.      | 1–2 est.    | 1–3 est.       | 1–1k+ flex.   |
| Shortest Symbol           | 1 phoneme    | single call    | single yip     | chirp         | scent pulse | grunt          | binary/unit   |
| Longest Symbol            | \~45 chars   | growl          | howl           | song-seq.     | scent chain | complex call   | infinite      |
| Most Frequent Symbol      | articles     | alarm          | bark           | tweet         | trail mark  | social ping    | tokens        |

---

#### Notes:

* **Machina** represents artificial systems with theoretically unlimited symbol rates and structural representations (vectors, matrices, codepoints).
* **Symbol Discern Rate** is analogous to WPM but scaled for species’ perceptual speed and bandwidth.
* “Distinct Symbol Types” reflects lexical diversity—though approximate, it suggests range and complexity.
* Aves show high perceptual speed with lower bandwidth, implying higher symbol compression and repetition (e.g., bird songs).
* Insecta rely more on pheromonal or vibration-based symbols (slow bandwidth, but high clarity).
* Humans show complex symbol combinations (words) and large corpus size due to rich sensory resolution.

---
Would you like to follow this table with an interpretation or visual diagram illustrating the compression vs. capacity trade-off per species?


---


## Chapter 7: Signal as Function — Symbols, Meaning, and Actors

In previous sections, we modeled language semiotically as a transmission of symbols and meanings. Here, we expand the model to include a third operand — **Actor** — representing the observable or latent result of the comprehension process.

### 🧮 Refined Mathematical Model of Symbolic Communication

We define the symbolic communication process as:

$$
\text{Signal}_{t} = f(\text{Symbol}_{t}, \text{Meaning}_{t}, \text{Actor}_{t})
$$

Where:

* **Symbol**: A perceivable structure in a sensory modality (e.g., sound, shape, smell)
* **Meaning**: The internalized representation or conceptual decoding of a symbol
* **Actor**: The effect of understanding — a choice, behavior, or other contextual output

We can break down this further:

$$
\text{Actor}_t = \phi(\text{Interpretation}_t, \text{Context}_t)
$$

$$
\text{Interpretation}_t = \psi(\text{Symbol}_t, \text{Meaning}_t)
$$

Thus:

$$
\text{Signal}_t = f\left(\text{Symbol}_t, \text{Meaning}_t, \phi\left(\psi(\text{Symbol}_t, \text{Meaning}_t), \text{Context}_t\right)\right)
$$

This allows us to model both:

* Internal processes (decoding symbols)
* External consequences (observable actions)

### 🧪 Example: Human Language

| Component   | Description                              | Human Metric Example                   |
| ----------- | ---------------------------------------- | -------------------------------------- |
| **Symbol**  | /faɪr/ → acoustic waveform, visual text  | Perceived at \~20–200 Hz auditory rate |
| **Meaning** | "Danger", "heat", "weapon", "excitement" | Chosen based on context, experience    |
| **Actor**   | Duck, run, smile, shout back, freeze     | Observable behavior (WPM, motor act)   |

### 📊 Mapping Against the Semiotic Table

| Class      | Speed (Hz) | Vision Bandwidth (Hz) | Hearing Bandwidth (Hz) | Field of View (°) | Resolution (WPM) | Symbol Count (est.) | Longest Word | Shortest Word | Most Frequent Word | Actor Space    |
| ---------- | ---------- | --------------------- | ---------------------- | ----------------- | ---------------- | ------------------- | ------------ | ------------- | ------------------ | -------------- |
| Human      | \~60       | \~0.4–60              | \~20–20,000            | \~210             | 150–200          | >100k symbols       | 12+          | 1             | "the"              | Extremely Rich |
| Felidae    | \~70       | \~0.1–55              | \~60–65,000            | \~200             | <10              | \~50–100            | 2–4 sounds   | 1 sound       | call/meow          | Narrow         |
| Canidae    | \~80       | \~0.1–50              | \~40–60,000            | \~250             | <10              | \~100               | 3–5 sounds   | 1 sound       | bark               | Narrow         |
| Aves       | \~100      | \~1–30                | \~1,000–4,000          | \~300             | \~15–30          | \~500–2,000 songs   | 8 chirps     | 1 chirp       | alarm chirp        | Medium         |
| Insecta    | \~120      | \~0.2–200 (motion)    | Low, <5,000            | \~300             | <5               | \~20 pheromones     | odor chains  | click/scent   | mating pheromone   | Simple         |
| Olfactores | \~70       | Scent-based           | Scent-based            | ?                 | ?                | \~50–100            | scent blends | base scent    | alert pheromone    | Narrow         |
| Machina    | 10–1000+   | all EM                | all EM                 | 360               | >10,000 WPM      | ∞ (byte-wise)       | unbounded    | 1-bit         | protocol sync byte | Fully Flexible |

### 🔁 Interpretation

The **Actor** is crucial to understanding not only whether a symbol was understood, but *how it was used*. Its addition allows for a complete loop:

1. **Symbol** transmitted (acoustic, EM, gesture)
2. **Meaning** formed (contextualized, personal, or shared)
3. **Actor** chosen (from an action space)

This framing also aligns closely with `SignalFrame`, where metadata fields capture actor outcomes:

* `action_triggered`
* `semantic_tags`
* `recipient_state_change`

In artificial systems, we can now observe the *full arc* from reception → understanding → result, enabling reverse-inference of meaning by analyzing outcomes.

---

## Chapter 8: Modeling Actor as Signal Operand

This chapter formalizes the third operand in symbolic communication: the **Actor**, representing the contextual outcome or response to understanding a symbol within a given context. Building upon the semiotic framework of `Symbol` and `Meaning`, we now extend our mathematical and conceptual model to include `Actor` as a probabilistic, dynamic operand.

### 📐 Expanded Mathematical Formulation

Let:

* `Symbol_t` be the perceivable form at time *t*
* `Meaning_t` be the interpretation generated by the receiver
* `Actor_t` be the context-driven choice or outcome

Then:

$$
\text{Signal}_t = f(\text{Symbol}_t, \text{Meaning}_t, \phi(\psi(\text{Symbol}_t, \text{Meaning}_t), \text{Context}_t))
$$

Where:

* $\psi$ maps Symbol and Meaning into an internal Interpretation
* $\phi$ maps that Interpretation into a behavioral response or semantic realization, given Context

This structure is recursive in systems that support feedback, self-awareness, or iterative interpretation.

### 📊 Symbol Capability Vector: Statistical Decomposition

To model symbol recognition and processing:

$$
\vec{S}_{\text{species}} = \begin{bmatrix}
\text{Perceptual Rate (Hz)} \\
\text{Vision Bandwidth (Hz)} \\
\text{Auditory Bandwidth (Hz)} \\
\text{Field of View (deg)} \\
\text{Perceptual Resolution (symbols/sec)}
\end{bmatrix}
$$

From this we derive a species-specific **Symbol Capacity Function**:

$$
C_s(\vec{S}) = \alpha_1 \cdot \text{Perceptual Rate} + \alpha_2 \cdot \log(\text{Vision BW}) + \alpha_3 \cdot \log(\text{Auditory BW}) + \alpha_4 \cdot \text{FOV} + \alpha_5 \cdot \text{Resolution}
$$

This provides an upper bound on the rate and complexity of symbols a species can process.

### 🔁 Meaning Compression Ratio

To compress conceptual space into symbolic channels, we define:

$$
MCR = \frac{|\text{Contextual Actions}|}{|\text{Available Symbols}|}
$$

* High $MCR$: Dense communication (e.g., bird alarm calls)
* Low $MCR$: Redundant, expansive communication (e.g., human speech)

### 🎯 Actor as Semantic Outcome

We model Actor as a distribution over possible outcomes:

$$
P(\text{Actor}_t | \text{Interpretation}_t, \text{Context}_t)
$$

This allows us to:

* Simulate behavioral outcomes from perceived signals
* Model ambiguity and action likelihoods
* Analyze how species or systems prioritize actions given meaning

In software terms, this can be logged via metadata fields in `SignalFrame` such as:

* `actor_choice`
* `outcome_probabilities`
* `triggered_behavior`

### 🧠 Interpretation as a Bridge

The inclusion of Actor closes the loop in communication:

1. Symbol is transmitted
2. Meaning is derived
3. Actor selects or generates an action

This enables predictive modeling and reverse-inference (e.g., deducing probable meaning from action alone), making it a key construct in signal semiotics.

>>In the next chapter, we will explore **Actor Field Design** — how to formalize, label, and structure actors across species, sensors, and artificial agents.

