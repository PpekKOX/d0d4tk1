from database import db
from datetime import datetime




class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    world = db.Column(db.String(32), nullable=False)

    level = db.Column(db.Integer)
    prof = db.Column(db.String(64))
    clan = db.Column(db.String(64))
    map = db.Column(db.String(64))
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    license = db.Column(db.String(64))
    status = db.Column(db.String(64))
    last_online = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint("name", "world", name="uniq_character_world"),
    )
