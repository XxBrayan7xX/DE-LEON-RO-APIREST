class BaseConfig:
    USER_DB='postgres'
    PASS_DB='admin'
    URL_DB='localhost'
    NAME_BD='parcial3'
    FULL_URL_DB=f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}'
    SQLALCHEMY_DATABASE_URI=FULL_URL_DB
    SECRET_KEY='llave_secreta'
    DEBUG = False
    BCRYPT