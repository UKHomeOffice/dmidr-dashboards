import re
from flask import redirect
from werkzeug.wrappers import Request, Response
import os
import json


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


class AuthMiddleware:
    def __init__(self, server, config_path=None):
        if config_path is None:
            config_path = os.path.join(os.path.dirname(__file__), "middleware.json")

        with open(config_path, "r") as f:
            config = json.load(f)

        # ToDo: Change this to something else
        server.config["SECRET_KEY"] = "SECRET"

        self.app = server.wsgi_app
        self.session_interface = server.session_interface
        self.server_config = Objectify(config=server.config, **server.config)
        self.login_uri = config["login-url"]
        self.whitelisted_urls = config["whitelisted-urls"]

    def __call__(self, environ, start_response):
        request = Request(environ)

        # If on a page which doesn't require authentication e.g. Login page
        if check_match_in_list(self.whitelisted_urls, request.path):
            return self.app(environ, start_response)

        # If we have a token continue,
        # otherwise want to redirect to login page
        if self.is_logged_in(request):
            return self.app(environ, start_response)

        res = redirect(self.login_uri)
        return res(environ, start_response)

    def is_logged_in(self, request):
        return "token" in self.session_interface.open_session(
            self.server_config, request
        )
