from peewee import *
from config import DB_FILE

db = SqliteDatabase(DB_FILE)

class user(Model):
    from_id = IntegerField(unique=True)
    first_name = CharField(max_length=50,default="Mavjud emas")
    last_name = CharField(max_length=50,default="Mavjud emas")
    user_name = CharField(max_length=50,default="Mavjud emas")

    class Meta:
        database = db

