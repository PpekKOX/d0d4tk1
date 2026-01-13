from database import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    world = db.Column(db.String(32), nullable=False)

    level = db.Column(db.Integer)
    map = db.Column(db.String(64))
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    last_online = db.Column(db.DateTime)

    __table_args__ = (
        db.UniqueConstraint("name", "world", name="uniq_character_world"),
    )
