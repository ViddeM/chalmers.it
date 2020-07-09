import os

import api
import config
from db import cleanse

clear_db = False

if not os.path.exists(config.FILE_SAVE_FOLDER):
    dirs = os.listdir(".")
    print("DIRS: " + str(dirs))
    raise (Exception('Directory not found: "%s"\n'
                     'Create the directory or change "config.py"' % config.FILE_SAVE_FOLDER))

if __name__ == '__main__':
    if clear_db:
        cleanse()

    api.run()
