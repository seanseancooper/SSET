# Semiotic Layer: Meaning, Context, Intent
# Interpret the signal as a communicative act. What system is speaking? What’s its intent or function?
#
# Emitter profiling: Who/what emits this?
# Temporal behavior: When and how often does it transmit?
# Spatial analysis: Where is it, where is it pointed?
# Intent modeling: What operational purpose is this signal serving?
#
# ### signal_semiotics_toolkit/semiotic/interpreter.py

class SignalInterpretation:
    # this encapsulates a result, right?


    def __init__(
        self,
        intent: Optional[str],
        activity_pattern: Optional[str],
        signal_bias_profile: Dict[str, Any],
        variance_features: Dict[str, Any],
        confidence: float
    ):
        self.intent = intent                            #
        self.activity_pattern = activity_pattern        # on what time scale? is this the entire analysis
        self.signal_bias_profile = signal_bias_profile
        self.variance_features = variance_features
        self.confidence = confidence                    # prediction, inference? idea: real-time sentiment & vocal stress analysis. Media Archeology
