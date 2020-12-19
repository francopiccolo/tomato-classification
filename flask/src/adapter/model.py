import tensorflow as tf

class ModelFile:
    def __init__(self, file_path):
        self.file_path = file_path

    @property
    def model(self):
        return tf.keras.models.load_model(self.file_path)