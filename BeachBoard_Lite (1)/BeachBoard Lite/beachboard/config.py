"""Application settings."""
import base64
import os 

SECRET_KEY = os.environ["BEACHBOARD_SECRET_KEY"] 
EXPORT_KEY = base64.b64decode(os.environ["BEACHBOARD_EXPORT_KEY"], validate=True)

if len(EXPORT_KEY) not in (16,24,32):
    raise ValueError("EXPORT_KEY must be decoded 16, 24, or 32 bytes")

