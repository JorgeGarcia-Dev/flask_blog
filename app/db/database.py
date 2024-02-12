# This is my Singleton Class to connect MySQL and Flask with:
# peewee, pymysql and python-decouple.

import peewee

from decouple import config


class MySQLDatabaseSingleton:
    """Singleton class to connect MySQL and Flask with peewee,
        pymysql and python-decouple.

    Attributes:
        database (peewee.MySQLDatabase): MySQL database.

    Methods:
        init_db(self)
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init_db()
        return cls._instance

    def init_db(self):
        """Initialize the database.

        Attributes:
            database (peewee.MySQLDatabase): MySQL database.
        """
        self.database = peewee.MySQLDatabase(
            database=config("DB_MYSQL"),
            host="localhost",
            user=config("USER_MYSQL"),
            password=config("PASSWORD_MYSQL"),
        )
