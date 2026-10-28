from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

SOCIETES = ["Frais Embal", "ChanadeMarée", "Comptoir des Pêcheurs Boulonnais"]
MAX_ENFANTS = 6


class Demande(db.Model):
    __tablename__ = "demandes"

    id = db.Column(db.Integer, primary_key=True)
    societe = db.Column(db.String(200), nullable=False)
    nom_salarie = db.Column(db.String(100), nullable=False)
    prenom_salarie = db.Column(db.String(100), nullable=False)
    enfant_commun = db.Column(db.Boolean, nullable=False, default=False)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    enfants = db.relationship(
        "Enfant", backref="demande", cascade="all, delete-orphan",
        order_by="Enfant.rang",
    )


class Enfant(db.Model):
    __tablename__ = "enfants"

    id = db.Column(db.Integer, primary_key=True)
    demande_id = db.Column(db.Integer, db.ForeignKey("demandes.id"), nullable=False)
    rang = db.Column(db.Integer, nullable=False)
    nom_prenom = db.Column(db.String(200), nullable=False)


class AdminUser(db.Model):
    __tablename__ = "admin_users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)


class Settings(db.Model):
    __tablename__ = "settings"

    id = db.Column(db.Integer, primary_key=True)
    deadline_date = db.Column(db.Date, nullable=True)
    enfants_nes_apres = db.Column(db.Date, nullable=False)
    hero_image_filename = db.Column(db.String(255), nullable=True)
    hero_image_mobile_filename = db.Column(db.String(255), nullable=True)
