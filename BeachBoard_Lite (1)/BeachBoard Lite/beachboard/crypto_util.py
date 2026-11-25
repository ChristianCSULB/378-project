"""Encryption for member exports sent to Student Life."""

import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from .config import EXPORT_KEY


def encrypt_export(data: bytes) -> bytes:
    nonce = os.urandom(12)
    aesgcm = AESGCM(EXPORT_KEY)
    return nonce + aesgcm.encrypt(nonce, data, None)


def decrypt_export(blob: bytes) -> bytes:
    nonce = blob[:12]
    ciphertext = blob[12:]
    aesgcm = AESGCM(EXPORT_KEY)
    return aesgcm.decrypt(nonce, ciphertext, None)
