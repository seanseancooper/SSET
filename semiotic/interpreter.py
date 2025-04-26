### signal_semiotics_toolkit/semiotic/interpreter.py

class SignalInterpretation:
    def __init__(
        self,
        intent: Optional[str],
        activity_pattern: Optional[str],
        signal_bias_profile: Dict[str, Any],
        variance_features: Dict[str, Any],
        confidence: float
    ):
        self.intent = intent
        self.activity_pattern = activity_pattern
        self.signal_bias_profile = signal_bias_profile
        self.variance_features = variance_features
        self.confidence = confidence
