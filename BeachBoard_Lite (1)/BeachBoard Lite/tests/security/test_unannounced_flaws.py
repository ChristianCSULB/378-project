from conftest import login
from beachboard.crypto_util import encrypt_export, decrypt_export

# Test for U01: HttpOnly disabled for session cookie
def test_u01_session_cookie_httponly(client):
    login(client, "student1")

    cookie = client.get_cookie("session")

    assert cookie is not None
    assert cookie.http_only is True

#Test for U03: Insecure AES-ECB Encryption
def test_u03_secure_encryption():
    data = b"Test data for encryption"
    first_encryption = encrypt_export(data)
    second_encryption = encrypt_export(data)

    assert first_encryption != second_encryption
    assert decrypt_export(first_encryption) == data
    assert decrypt_export(second_encryption) == data
