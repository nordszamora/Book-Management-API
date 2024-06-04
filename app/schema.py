from flask_marshmallow import Marshmallow
from marshmallow import fields, validates, ValidationError
from app.models import Auth, Book
from . import create_app

ma = Marshmallow(create_app)

class AuthSchema(ma.SQLAlchemySchema):
   class Meta:
      model = Auth
   
   id = ma.auto_field()
   username = fields.Str(required=True)
   password = fields.Str(required=True)

   @validates('username')
   def validate_username(self, value):
       if len(value) < 4 or len(value) > 15:
          raise ValidationError('Username must be between 4 and 15 characters long.')
       
   @validates('password')
   def validate_password(self, value):
       if len(value) < 8:
          raise ValidationError('Password must be at least 8 characters long.')

class BookSchema(ma.SQLAlchemySchema):
   class Meta:
      model = Book

   id = ma.auto_field()
   isbn = fields.Int(required=True)
   title = fields.Str(required=True)
   author = fields.Str(required=True)
   genre = fields.Str(required=True)
   year = fields.Int(required=True)
   publisher = fields.Str(required=True)
   quantity = fields.Int(required=True)
   price = fields.Int(required=True)

   @validates('isbn')
   def validate_isbn(self, value):
       if value < 0:
          raise ValidationError('ISBN must be not negative.')
       
       elif value > 10000000000000:
          raise ValidationError('ISBN must be between 10 and 13 digits.')
       
   @validates('year')
   def validate_year(self, value):
       if value < 0:
          raise ValidationError('Year must be not negative.')
       
   @validates('quantity')
   def validate_quantity(self, value):
       if value < 0:
          raise ValidationError('Quantity must be not negative.')
   
   @validates('price')
   def validate_price(self, value):
       if value < 0:
          raise ValidationError('Price must be not negative.')
       