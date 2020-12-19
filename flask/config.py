import os

STAGE = os.environ.get('STAGE')

class Config:
    CLASS_NAMES = ['Plum', 'Cherry', 'BeefSteak']
    MODEL_FILE_PATH = 'data/tomato_model.h5'

    @classmethod
    def init_app(cls, app):
        pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    pass

class ProdConfig(Config):
    pass

config = {
    'test': TestConfig,
    'dev': DevConfig,
    'prod': ProdConfig
}

config = config[STAGE]