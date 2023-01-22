from typing import Optional
import os

SQLALCHEMY_DATABASE_URL = os.environ.get("CLEARDB_DATABASE_URL")
MAIL_SENDER = os.environ.get("MAIL_SENDER")
MAIL_PASSWARD = os.environ.get("MAIL_PASSWARD")
BACKEND_SERVER_URL = os.environ.get("BACKEND_SERVER_URL")
DISCORD_WEBHOOKS_NEW_POST_UPLOAD_LOG = os.environ.get("DISCORD_WEBHOOKS_NEW_POST_UPLOAD_LOG")
DISCORD_WEBHOOKS_POST_UPDATE_LOG = os.environ.get("DISCORD_WEBHOOKS_POST_UPDATE_LOG")
GOOGLE_API_KEY: str = os.environ.get("GOOGLE_API_KEY")
GOOGLE_SEARCH_ENGINE_ID: str = os.environ.get("GOOGLE_SEARCH_ENGINE_ID")
LAUNCH_MODE: Optional[str] = os.environ.get("LAUNCH_MODE")
