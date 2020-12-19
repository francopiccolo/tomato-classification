from flask import request

from config import config
from service.service import predict, InvalidInput
from adapter.model import ModelFile
from api.v1 import bp

model_file = ModelFile(config.MODEL_FILE_PATH)

@bp.route('/predict', methods=['POST'])
def predict_api():
    input = request.json
    try:
        predictions = predict(input, model_file)
    except InvalidInput as e:
        return str(e), 400
    return predictions