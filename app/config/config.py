from enum import Enum


class Config(Enum):

    DATABASE = "mysql+pymysql://root:admin@localhost:3306/db_hosts"
    

    