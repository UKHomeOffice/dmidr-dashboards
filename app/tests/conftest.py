import pytest
import os

from app.authentication.auth_middleware import AuthMiddleware
from app.tests.authentication.auth_middleware.test_flask_app import create_app


@pytest.fixture()
def app():
    middleware_config_dir = os.path.join(
        os.path.dirname(__file__), "authentication/auth_middleware/test_middleware.json"
    )

    app = create_app()
    app.config.update({"TESTING": True})
    app.wsgi_app = AuthMiddleware(app, middleware_config_dir)

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
