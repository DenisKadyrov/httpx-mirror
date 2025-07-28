import os


class Config:
    """
    Application configurations

    """
    def __init__(self):
        self.BASE_URL = os.getenv('BASE_URL')

        if not self.BASE_URL:
            raise ValueError("Missing required environment variable: BASE_URL")

        self.DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'

