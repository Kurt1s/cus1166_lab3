import os
basedir = os.path.abspath(os.path.dirname(__file__))

'sqlite:///' + os.path.join(basedir, 'app.db')

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    