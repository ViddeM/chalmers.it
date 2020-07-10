import os
import uuid
from datetime import datetime

from pony.orm import db_session

import config
from db import FileEntry

upload_folder = config.FILE_SAVE_FOLDER


@db_session
def store_file_in_db(file: str) -> uuid:
    now = datetime.utcnow()
    file_entity = FileEntry(file_link="Trevligt", upload_time=now)
    file_id = file_entity.file_id
    file_directory = str.format("{0}/{1}/{2}", upload_folder, file_id, file.filename)

    file_entity.file_link = file_directory

    if not os.path.exists(file_directory):
        os.makedirs(file_directory)

    file.save(os.path.join(file_directory, file.filename))

    return file_id


@db_session
def retrieve_file_link(file_id: str) -> str:
    file_entity = FileEntry.get(file_id=file_id)
    return file_entity.file_link