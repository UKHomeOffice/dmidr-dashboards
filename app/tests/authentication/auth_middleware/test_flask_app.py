from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/login")
    def login_page():
        return "login page"

    @app.route("/")
    def home_page():
        return "home page"

    @app.route("/whitelisted")
    def whitelist_page():
        return "whitelisted page"

    return app
