import os
from databases import Database

DATABASE_URL = f"sqlite:///./database.db"
database = Database(DATABASE_URL)
