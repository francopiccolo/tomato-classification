from flask import Blueprint

bp = Blueprint('api', __name__) # This is here to avoid circular dependency

from api.v1.predict import predict