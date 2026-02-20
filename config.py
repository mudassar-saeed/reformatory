import os


class Config:
    # -------------------------------
    # Basic App Settings
    # -------------------------------

    SECRET_KEY = "reformatory_secret_key"

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # -------------------------------
    # File Upload Settings
    # -------------------------------

    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
    OUTPUT_FOLDER = os.path.join(BASE_DIR, "outputs")

    ALLOWED_EXTENSIONS = {"pdf"}

    # Max file size: 10MB
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024
