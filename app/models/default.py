from app.extensions import db


class Default(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Employer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    default_id = db.Column(db.ForeignKey('default.id'))
