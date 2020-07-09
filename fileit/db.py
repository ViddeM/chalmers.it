import uuid
from datetime import datetime

from pony.orm import Database, PrimaryKey, Required, db_session

import config

db = Database()
db.bind(
    provider='postgres',
    user=config.POSTGRES_USER,
    password=config.POSTGRES_PASSWORD,
    host=config.POSTGRES_HOST,
    port=config.POSTGRES_PORT,
    database=config.POSTGRES_DB
)


class FileEntry(db.Entity):
    file_id = PrimaryKey(uuid.UUID, auto=True)
    file_link = Required(str)
    upload_time = Required(datetime)


db.generate_mapping(create_tables=True)


@db_session
def cleanse():
    db.execute("DROP SCHEMA public CASCADE;")
    db.execute("CREATE SCHEMA public;")