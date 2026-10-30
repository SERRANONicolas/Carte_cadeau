import os
from datetime import date


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "changeme-en-production")
    SQLALCHEMY_DATABASE_URI = "sqlite:////app/data/cartes_cadeaux.db"
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    PERMANENT_SESSION_LIFETIME = 8 * 3600
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "changeme")

    # Valeurs de départ, seedées en base au premier démarrage puis modifiables depuis /admin/settings
    DEFAULT_DEADLINE_DATE = None
    DEFAULT_ANNEE = 2026
    DEFAULT_ENFANTS_NES_APRES = date(2014, 1, 1)

    UPLOAD_DIR = "/app/data/uploads"
    HERO_IMAGE_MAX_BYTES = 8 * 1024 * 1024
    HERO_IMAGE_ALLOWED_EXT = (".jpg", ".jpeg", ".png", ".webp")
    HERO_IMAGE_IDEAL_RESOLUTION = "1920 × 1280 px minimum, format paysage"
    HERO_IMAGE_MOBILE_IDEAL_RESOLUTION = "1080 × 1920 px minimum, format portrait"
