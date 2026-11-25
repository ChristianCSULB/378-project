from conftest import login

def test_u01_session_cookie_httponly(client):
    login(client, "student1")

    cookie = client.get_cookie("session")

    assert cookie is not None
    assert cookie.http_only is True

