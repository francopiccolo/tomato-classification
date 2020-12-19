from flask import Flask

from config import config
from api.v1 import bp as api_bp

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    config.init_app(app)
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    return app

if __name__ == '__main__':
    app = create_app(config)
    app.run(host='0.0.0.0', debug=True)