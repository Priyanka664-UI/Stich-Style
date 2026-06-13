import firebase_admin
from firebase_admin import credentials
import json
from app.config.settings import settings
import logging

logger = logging.getLogger(__name__)

def initialize_firebase():
    try:
        cred_dict = json.loads(settings.FIREBASE_CREDENTIALS_JSON)
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred)
        logger.info("Firebase initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize Firebase: {e}")
