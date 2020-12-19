from domain.model import Model

class InvalidInput(Exception):
    def __str__(self):
        return 'Invalid input'

def predict(input, model_adapter):
    model = Model(model_adapter.model)
    try:
        predictions = model.predict(input)
    except Exception:
        raise InvalidInput

    return predictions