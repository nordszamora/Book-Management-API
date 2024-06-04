class Config:
   SQLALCHEMY_DATABASE_URI = 'mysql://user:pass@host:port/db'
   SECRET_KEY = 'secret-key'
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   JWT_SECRET_KEY = 'jwt-secret-key'
   