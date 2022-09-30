import json
import os.path

from flask import session
from keycloak import KeycloakOpenID, KeycloakAuthenticationError


class KeycloakAuth:
    def __init__(self, config_path=None):
        if config_path is None:
            config_path = os.path.join(os.path.dirname(__file__), "keycloak.json")

        with open(config_path, "r") as f:
            config_data = json.load(f)

        # Set up the Keycloak connection.
        keycloak_config = dict(
            server_url=config_data["auth-server-url"],
            realm_name=config_data["realm"],
            client_id=config_data["credentials"]["client_id"],
            client_secret_key=config_data["credentials"]["secret"],
            verify=config_data["ssl-required"] != "none",
        )

        self.keycloak_openid = KeycloakOpenID(**keycloak_config)

    def login(self, username, password):
        try:
            token = self.keycloak_openid.token(username, password)
            userinfo = self.keycloak_openid.userinfo(token["access_token"])
            session["token"] = token
            session["userinfo"] = userinfo
            return
        except KeycloakAuthenticationError:
            return "Username and password are incorrect."

    def decode_token(self):
        keycloak_public_key = (
            f"-----BEGIN PUBLIC KEY-----\n"
            + self.keycloak_openid.public_key()
            + "\n-----END PUBLIC KEY-----"
        )
        options = {"verify_signature": True, "verify_aud": False, "verify_exp": True}
        token_info = self.keycloak_openid.decode_token(
            self.token["access_token"], key=keycloak_public_key, options=options
        )
        return token_info
