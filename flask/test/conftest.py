import pytest

from config import config
from adapter.model import ModelFile

@pytest.fixture()
def model():
    return ModelFile(config.MODEL_FILE_PATH).model

@pytest.fixture()
def model_adapter():
    return ModelFile(config.MODEL_FILE_PATH)

@pytest.fixture()
def input():
    return [
        [5.1, 3.3, 1.7, 0.5],
        [5.9, 3.0, 4.2, 1.5],
        [6.9, 3.1, 5.4, 2.1]
    ]