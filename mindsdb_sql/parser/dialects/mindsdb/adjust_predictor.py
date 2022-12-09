from .create_predictor import CreatePredictorBase


class AdjustPredictor(CreatePredictorBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._command = 'ADJUST'