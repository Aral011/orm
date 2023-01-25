import peewee
from peewee import PostgresqlDatabase
from datetime import datetime


db = PostgresqlDatabase(
    'orm_py25',
    user='hello',
    password='1',
    host='localhost',   # где размещенна субд, он локально(у нас на компьютере)
    port=5432     # окошко, порт
)




db.connect()