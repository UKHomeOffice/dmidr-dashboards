import pytest

from app.authentication.auth_middleware import AuthMiddleware
from authentication.test_flask_app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {"TESTING": True,}
    )
    app.wsgi_app = AuthMiddleware(app, "test_middleware.json")

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
