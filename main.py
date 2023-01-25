

from views import *
from settings import db

db.connect()

get_categories()
get_products()