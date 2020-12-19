import pytest

from config import config
from service.service import predict, InvalidInput

def test_predict(input, model_adapter):
    response = predict(input, model_adapter)
    assert response ['classes'] == config.CLASS_NAMES

def test_bad_input(model_adapter):
    input = []
    with pytest.raises(InvalidInput):
        predict(input, model_adapter)

    input = [1, 1, 1, 1]
    with pytest.raises(InvalidInput):
        predict(input, model_adapter)

    input = [[1, 1, 1]]
    with pytest.raises(InvalidInput):
        predict(input, model_adapter)