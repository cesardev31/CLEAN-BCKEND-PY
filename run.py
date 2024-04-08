from flask import Flask
from config import config
from app.controllers.user_controller import user_controller

app = Flask(__name__)


def page_not_found(error):
    return "<h1>Not found page</h1>", 404


if __name__ == "__main__":
    app.config.from_object(config["development"])

    app.register_blueprint(user_controller)

    app.register_error_handler(404, page_not_found)

    app.run()
