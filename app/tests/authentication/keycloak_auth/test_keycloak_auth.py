import os

from app.authentication.keycloak_auth import KeycloakAuth
from keycloak import KeycloakOpenID, KeycloakAuthenticationError

from flask import session

test_config_dir = os.path.join(os.path.dirname(__file__), "test_keycloak.json")


def test_keycloak_auth_can_create():
    """Test keycloak auth object can be created with config path"""
    KeycloakAuth(test_config_dir)


def test_keycloak_auth_login_adds_auth_data_to_session_when_login_success(
    app, monkeypatch
):
    """Test login works when provided with username and password"""

    def token_mock(self, username, password):
        return {"access_token": "TOKEN"}

    def userinfo_mock(self, token):
        return "user info"

    monkeypatch.setattr(KeycloakOpenID, "token", token_mock)
    monkeypatch.setattr(KeycloakOpenID, "userinfo", userinfo_mock)

    # Having to create a test request context as keycloak auth access session
    with app.test_request_context():
        keycloak_auth = KeycloakAuth(test_config_dir)
        msg = keycloak_auth.login("", "")
        assert not msg
        assert "token" in session
        assert "userinfo" in session


def test_keycloak_auth_login_returns_error_msg_with_invalid_credentials(
    app, monkeypatch
):
    """Test login works when provided with username and password"""

    def token_mock(self, username, password):
        raise KeycloakAuthenticationError("Invalid credentials")

    monkeypatch.setattr(KeycloakOpenID, "token", token_mock)

    # Having to create a test request context as keycloak auth access session
    with app.test_request_context():
        keycloak_auth = KeycloakAuth(test_config_dir)
        msg = keycloak_auth.login("", "")
        assert "Username and password are incorrect." in msg
