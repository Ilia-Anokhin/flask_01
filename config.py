class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root@localhost:3306/test1'
    #SECRET_KEY='fak'