import tensorflow as tf

from config import config

class Model:
    def __init__(self, model):
        self.model = model

    def pre_process(self, input):
        return tf.convert_to_tensor(input)

    def post_process(self, predictions):
        array = predictions.numpy()
        return array.tolist()

    def predict(self, input):
        input = self.pre_process(input)
        predictions = self.model.predict(input)
        predictions = tf.nn.softmax(predictions)
        predictions = self.post_process(predictions)

        return {'classes': config.CLASS_NAMES,
                'predictions': predictions}