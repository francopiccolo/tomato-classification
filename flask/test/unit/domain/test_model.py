from config import config
from domain.model import Model

def test_predict(model, input):
    response = Model(model).predict(input)
    assert response['classes'] == config.CLASS_NAMES
    assert isinstance(response['predictions'][0], list)
    assert len(response['predictions']) == len(config.CLASS_NAMES)
    assert isinstance(response['predictions'][0][0], float)
