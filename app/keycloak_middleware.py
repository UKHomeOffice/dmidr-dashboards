from flask import redirect
from werkzeug.wrappers import Request, Response
from keycloak import KeycloakOpenID, KeycloakAuthenticationError


class Objectify(object):
    def __init__(self, **kwargs):
        self.__dict__.update({key.lower(): kwargs[key] for key in kwargs})


class KeycloakMiddleware:
    def __init__(self, server, keycloak_openid: KeycloakOpenID):
        # ToDo: Change this to something else
        server.config["SECRET_KEY"] = "SECRET"

        self.app = server.wsgi_app
        self.session_interface = server.session_interface
        self.config = server.config
        self.config_object = Objectify(config=self.config, **self.config)
        self.keycloak_openid = keycloak_openid
        self.login_submit_url = "/login-submit"
        self.redirect_url = "/"
        self.whitelisted_urls = [
            "/login",
            "/assets/style.css",
            "/assets/govuk-frontend-4.3.1.min.css",
            "/assets/govuk-frontend-ie8-4.3.1.min.css",
            "/assets/images/favicon.ico",
            "/_reload-hash",
            "/_dash-dependencies",
            "/_dash-update-component",
            "/_dash-layout",
            "/_dash-component-suites/dash/dash_table/bundle.js.map",
            "/_dash-component-suites/dash/html/dash_html_components.min.js.map",
            "/_dash-component-suites/dash/dash-renderer/build/dash_renderer.v2_6_1m1664181030.dev.js",
            "/_dash-component-suites/dash/dcc/dash_core_components-shared.v2_6_1m1664181031.js",
            "/_dash-component-suites/dash/html/dash_html_components.v2_0_5m1664181031.min.js",
            "/_dash-component-suites/dash/dash_table/bundle.v5_1_5m1664181030.js",
            "/_dash-component-suites/dash/dcc/dash_core_components.v2_6_1m1664181031.js",
            "/_dash-component-suites/dash/deps/prop-types@15.v2_6_1m1664181031.8.1.js",
            "/_dash-component-suites/dash/deps/react-dom@16.v2_6_1m1664181031.14.0.js",
            "/_dash-component-suites/dash/deps/react@16.v2_6_1m1664181031.14.0.js",
            "/_dash-component-suites/dash/deps/polyfill@7.v2_6_1m1664181031.12.1.min.js",
        ]

    def __call__(self, environ, start_response):
        request = Request(environ)

        # If on a page which doesn't require authentication
        if request.path in self.whitelisted_urls:
            return self.app(environ, start_response)

        # If we have a token continue
        # Otherwise want to redirect to new page
        # ToDo: Include redirect
        if self.is_logged_in(request):
            return self.app(environ, start_response)

        # Only check for credentials on login page
        if request.path == self.login_submit_url:
            username = request.authorization["username"]
            password = request.authorization["password"]

            try:
                token = self.keycloak_openid.token(username, password)
                res = redirect(self.redirect_url)
                self.set_session(request, res, token=token)
                return res(environ, start_response)
            except KeycloakAuthenticationError:
                res = Response(u"Unauthorised", mimetype="text/plain", status=401)
                return res(environ, start_response)

        res = Response(u"Unauthorised", mimetype="text/plain", status=401)
        # res = redirect("http://localhost:8050/login")
        return res(environ, start_response)

    def is_logged_in(self, request):
        return "token" in self.session_interface.open_session(
            self.config_object, request
        )

    def set_session(self, request, response, **kwargs):
        session = self.session_interface.open_session(self.config_object, request)
        for kw in kwargs:
            session[kw] = kwargs[kw]
        self.session_interface.save_session(self.config_object, session, response)
        return response
