class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root@localhost:3306/test1'
    SECRET_KEY='fakghhh'

    SECURITY_PASSWORD_SALT='SALT'
    SECURITY_PASSWORD_HASH='sha512_crypt'
