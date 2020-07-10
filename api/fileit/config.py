import os

# SAVED FILES SETTINGS
FILE_SAVE_FOLDER = os.environ.get('FILEIT_SAVE_FOLDER', './files')
FILE_SIZE_CAP_BYTES = int(os.environ.get('FILEIT_FILE_SIZE_CAP_BYTES', 10 * 1024 * 1024))

# ALLOWED_EXTENSIONS = {e.strip() for e in os.environ.get('FILEIT_ALLOWED_EXTENSIONS', "png, jpg, jpeg, gif").split(",")}

# POSTGRES SETTINGS
POSTGRES_USER = os.environ.get('FILEIT_POSTGRES_USER', 'fileit')
POSTGRES_PASSWORD = os.environ.get('FILEIT_POSTGRES_PASSWORD', 'password')
POSTGRES_HOST = os.environ.get('FILEIT_POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.environ.get('FILEIT_POSTGRES_PORT', '5432')
POSTGRES_DB = os.environ.get('FILEIT_POSTGRES_DB', 'fileit')


