import re
from flask import redirect
from werkzeug.wrappers import Request, Response
from keycloak import KeycloakOpenID, KeycloakAuthenticationError


class Objectify(object):
    def __init__(self, **kwargs):
        self.__dict__.update({key.lower(): kwargs[key] for key in kwargs})


def check_match_in_list(patterns, to_check):
    if patterns is None or to_check is None:
        return False
    for pattern in patterns:
        if re.search(pattern, to_check):
            return True
    return False


class KeycloakMiddleware:
    def __init__(self, server, keycloak_openid: KeycloakOpenID):
        # ToDo: Change this to something else
        server.config["SECRET_KEY"] = "SECRET"

        self.app = server.wsgi_app
        self.session_interface = server.session_interface
        self.config = server.config
        self.config_object = Objectify(config=self.config, **self.config)
        self.keycloak_openid = keycloak_openid
        self.redirect_url = "/"
        self.login_uri = "/login"
        self.whitelisted_urls = [
            "/login",
            "/assets/*",
            "/_reload-hash",
            "/_dash-dependencies",
            "/_dash-update-component",
            "/_dash-layout",
            "/_dash-component-suites/*",
        ]

    def __call__(self, environ, start_response):
        request = Request(environ)

        # If on a page which doesn't require authentication e.g. Login page
        if check_match_in_list(self.whitelisted_urls, request.path):
            return self.app(environ, start_response)

        # If we have a token continue
        # Otherwise want to redirect to new page
        if self.is_logged_in(request):
            return self.app(environ, start_response)

        res = redirect(self.login_uri)
        return res(environ, start_response)

    def is_logged_in(self, request):
        return "token" in self.session_interface.open_session(
            self.config_object, request
        )
