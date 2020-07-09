import os

# SECURITY
API_KEY = os.environ.get('IMAGEIT_API_KEY', 'SUPERSECRETKEY')

# SAVED IMAGES SETTINGS
IMAGE_FOLDER = os.environ.get('IMAGEIT_IMAGE_FOLDER', './images')
IMAGE_SIZE_CAP_BYTES = int(os.environ.get('IMAGEIT_IMAGE_SIZE_CAP_BYTES', 10 * 1024 * 1024))
ALLOWED_EXTENSIONS = {e.strip() for e in os.environ.get('IMAGEIT_ALLOWED_EXTENSIONS', "png, jpg, jpeg, gif").split(",")}

# POSTGRES SETTINGS
POSTGRES_USER = os.environ.get('IMAGEIT_POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.environ.get('IMAGEIT_POSTGRES_PASSWORD', 'password')
POSTGRES_HOST = os.environ.get('IMAGEIT_POSTGRES_HOST', 'db')
POSTGRES_PORT = os.environ.get('IMAGEIT_POSTGRES_PORT', '5432')
POSTGRES_DB = os.environ.get('IMAGEIT_POSTGRES_DB', 'postgres')


