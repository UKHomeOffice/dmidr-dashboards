def test_request_redirect_when_not_authenticated(client):
    """Test requests are redirected when not authenticated"""
    response = client.get("/", follow_redirects=True)
    assert b"login page" in response.data


def test_request_does_not_redirect_when_token_in_session(client):
    """Test requests are not redirected when session contains token"""
    with client.session_transaction(subdomain="blue") as session:
        session["token"] = "TOKEN"

    response = client.get("/", follow_redirects=True)
    assert b"home page" in response.data


def test_request_to_whitelist_url_does_not_redirect_without_authentication(client):
    """Test requests to whitelisted urls do not need to be authenticated"""
    response = client.get("/whitelisted", follow_redirects=True)
    assert b"whitelisted page" in response.data
