from starlette.config import Config

config = Config(".env")

PROJECT_NAME = "Prototyp File System"
VERSION = "1.0.0"

SQLITE_DB_FILE = config('SQLITE_DB_FILE' ,cast=str, default=f'./db/db.sqlite3')
SQLITE_URL = config(
  'SQLITE_URL',
  cast=str,
  default=f'sqlite://{SQLITE_DB_FILE}'
)  
