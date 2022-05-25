from distutils.debug import DEBUG
import os

class Config:
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  DEBUG = False