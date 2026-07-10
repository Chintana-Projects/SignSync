"""
config.py

Application configuration.

Responsibilities:
- Store application settings
- Centralize configurable values
"""


class Settings:
    """
    Application settings.
    """

    APP_NAME = "SignSync"

    VERSION = "1.0.0"

    DEBUG = True


settings = Settings()