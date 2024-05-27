from . import db

class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   isbn = db.Column(db.BigInteger, unique=True, nullable=True)
   title = db.Column(db.String(255), nullable=True)
   author = db.Column(db.String(255), nullable=True)
   genre = db.Column(db.String(255), nullable=True)
   year = db.Column(db.Integer, nullable=True)
   publisher = db.Column(db.String(255), nullable=True)
   quantity = db.Column(db.Integer, nullable=True)
   price = db.Column(db.Integer, nullable=True)
